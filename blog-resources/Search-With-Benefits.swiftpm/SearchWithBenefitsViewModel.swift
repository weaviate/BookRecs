//
//  SearchWithBenefitsViewModel.swift
//  SearchWithBenefits
//
//  Created by Randy Fong on 4/24/24.
//

import Foundation

struct BookResponse: Decodable {
    let data: DataResponse
    
    struct DataResponse: Decodable {
        let Get: BookGetResponse
        
        struct BookGetResponse: Decodable {
            let Book: [Book]
        }
    }
}

struct Book: Decodable {
    let title: String
    let description: String
}

class SearchWithBenefitsViewModel: ObservableObject {
    @Published var books: [Book] = []
    @Published var message: String? = ""
    
    func getBooks(matching prompt: String) async {
        
        // URL and API Keys
        let urlString        = "https://zxzyqcyksbw7ozpm5yowa.c0.us-west2.gcp.weaviate.cloud/v1/graphql"
        let weaviateApiKey   = "n6mdfI32xrXF3DH76i8Pwc2IajzLZop2igb6"
        let openAiApiKey     = "<< Enter your OpenAI Key here >>"
        
        let urlRequest: URLRequest = {
            
            // URL
            let url = URL(string: urlString)!
            
            // Prompt
            let concepts = [prompt]
            let queryString = formatQuery(prompt: concepts)
            let queryData = queryString.data(using: .utf8)
            
            // URLRequest
            var urlRequest = URLRequest(url: url)
            urlRequest.httpMethod = "POST"
            urlRequest.setValue("application/json", forHTTPHeaderField: "Content-Type")
            urlRequest.setValue("Bearer \(weaviateApiKey)", forHTTPHeaderField: "Authorization")
            urlRequest.setValue(openAiApiKey, forHTTPHeaderField: "X-OpenAI-Api-Key")
            urlRequest.httpBody = queryData
            
            // Create URL Session
            return urlRequest
        }()
        
        do {
            // Loading Display
            await MainActor.run {
                books.removeAll()
                message = "Loading...."
            }
            
            // Get Books and Decode
            let (data, _) = try await URLSession.shared.data(for: urlRequest)
            let bookResponse: BookResponse = try JSONDecoder().decode(BookResponse.self, from: data)
            
            let booksFound = bookResponse.data.Get.Book
            if booksFound.count == 0 {
                // No Books Found Display
                message = "Unable to find related books"
            } else {
                // Books Found Display
                await MainActor.run {
                    message = nil
                    books = booksFound
                }
//                print("** Books")
//                debugPrint(books)
            }
        } catch(let error) {
            // Error Display
            await MainActor.run {
                message = "Search Error"
            }
            print("** Error")
            print(error)
        }
    }
}

// Format Weaviate Query
private func formatQuery(prompt concepts: [String], limit: Int = 10) -> String {
    let conceptsString = concepts.joined(separator: ", ")
    let formatString = """
                          {"query": "{Get {Book(limit: %@ nearText: {concepts: [\\"%@\\"]}) {title description _additional {certainty distance}}}}"}
                         """
    return String(format: formatString, String(limit), conceptsString)
}

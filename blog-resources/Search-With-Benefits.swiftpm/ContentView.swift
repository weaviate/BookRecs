//
//  ContentView.swift
//  SearchWithBenefits
//
//  Created by Randy Fong on 4/24/24.
//

import SwiftUI

struct ContentView: View {
    @StateObject var searchWithBenefitsViewModel = SearchWithBenefitsViewModel()
    @State var prompt: String = "" 
    var body: some View {
        VStack {
            Text(searchWithBenefitsViewModel.message ?? "").padding()
            HStack {
                TextField(
                    "Enter Prompt",
                    text: $prompt, axis: .vertical).textFieldStyle(.roundedBorder)
                Button {
                    Task {
                        await searchWithBenefitsViewModel.getBooks(matching: prompt)
                    }
                } label: {
                    Image(systemName: "magnifyingglass")
                }
                Button {
                    prompt = " "
                } label: {
                    Image(systemName: "clear")
                }
            }
            .padding()
            List(searchWithBenefitsViewModel.books, id: \.title) { book in
                Text(book.title)
                Text(book.description).font(.caption)
            }
        }
    }
}

/* 
 
 Suggested Prompts to Tryout
 
 1. Find similar books to Pride and Prejudice by Jane Austen.
 2. Find science fiction books similar to Dune by Frank Herbert.
 3. Find fantasy novels with a coming-of-age theme.
 4. Recommend dramas similar to Wizard of Oz.
 5. Search for mysteries set in Western Europe.
 6. Discover historical books similar to The Audacity of Hope: Thoughts on Reclaiming the American Dream.
 7. Personalize search results based on a college aged woman from Boston majoring in fine arts who enjoys vacations in France.
 8. Find books with a similar writing style to a JR Tolkien.
 9. Search for light-hearted comedies similar to a Tom Hanks movie like Forrest Gump.
 10. Recommend books with a similar emotional impact to Danielle Steel's The Butler.
 11. Assist book clubs by finding thematically linked books to The Anxious Generation: How the Great Rewiring of Childhood Is Causing an Epidemic of Mental Illness.
 12. Personalize children's book recommendations based on a kindergarten reading level.
 
 */

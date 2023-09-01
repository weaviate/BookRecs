export interface Book {
  isbn13: string;
  isbn10: string;
  title: string;
  subtitle: string;
  authors: string;
  categories: string;
  thumbnail: string;
  description: string;
  published_year: string;
  average_rating: string;
  num_pages: string;
  ratings_count: string;
}


export interface NearTextType {
  concepts: [string] | [];
  certainty?: number;
  moveAwayFrom?: object;
}

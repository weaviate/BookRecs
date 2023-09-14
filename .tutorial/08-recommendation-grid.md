## Displaying Recommendations

Once the semantic search is performed and the results are obtained, the recommended books are displayed on the application interface. The recommendation grid appears with a list of books that come from the semantic search result from our `nearText` query. These are stored in `recommendedBooks` after a query is made.

### Rendering Recommendations
In the JSX of `index`, we map through `recommendedBooks` which returns the relevant `divs` that represent the recommendations grid. The grid is styled in a `flex-wrap` `div` so that they expand into the parent container and wrap around when a row is filled.

### Displaying Book Details
As we map through those recommendations, we render book details to the screen such as the book thumbnail, the book title, and a button to learn more about the book.

### Rendering Modal
When the 'Learn More' button is tapped, a modal is rendered on the screen. There is some logic that will select the book and put it into the state for the modal to display, and then some additional state to force the modal to come on the screen.

---
*Note: The next section of the tutorial will include detailed steps on closing the modal and wrapping up the application.*

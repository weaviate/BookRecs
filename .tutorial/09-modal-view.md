## Modal Mechanics

In this section, we will briefly look at how the modal is triggered and what it includes.

### Opening the Modal
When the 'Learn More' button is clicked, the `openModal` function is triggered and receives a string that we can use to find the selected book. Once we've found it, we can set a state value for the book that was selected.

### Managing Modal Viewability
We'll also have a state variable to manage the viewability of the modal, we'll call it `modalIsOpen`. When this state is true, we render the modal to screen and that render logic is handled in the return portion of the component.

### Modal Content
This modal includes a thumbnail of the book, the author details, genre, average rating, published year, and description - these are rendered from the `selectedBook` state variable. Since we also have an International Standard Book Number or ISBN for this book, we can make a naive query against Amazon to show that book on an Amazon search result when clicked. This is mostly just for fun.

### Closing the Modal
Lastly, we'll include a `closeModal` button that will close the modal from view.

---
*Note: The next section of the tutorial will include detailed steps on finalizing and testing the application.*

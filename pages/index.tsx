import { SyntheticEvent, useState } from 'react';
import CircleLoader from 'react-spinners/CircleLoader';
import Modal from 'react-modal';
import { Book } from 'types';
const customStyles = {
  content: {
    top: '50%',
    left: '50%',
    right: 'auto',
    bottom: 'auto',
    marginRight: '-50%',
    width: '90%',
    height: '80%',
    transform: 'translate(-50%, -50%)',
    borderRadius: '5px',
  },
};
export default function Home() {
  const [isLoading, setIsLoading] = useState(false);
  const [loadedOnce, setLoadedOnce] = useState(false);
  const [query, setQuery] = useState('');
  const [recommendedBooks, setRecommendedBooks] = useState([]);
  const [modalIsOpen, setIsOpen] = useState(false);
  const [selectedBook, setSelectedbook] = useState<Book | undefined>(undefined);

  const openModal = (book_title: string) => {
    const bookSelection = recommendedBooks.filter((book: Book) => {
      return book.title === book_title;
    });
    console.log(bookSelection);
    setSelectedbook(bookSelection[0]);
    setIsOpen(true);
  };

  const closeModal = () => {
    setIsOpen(false);
  };

  const getRecommendations = async (e: SyntheticEvent) => {
    e.preventDefault();

    // Check Inputs
    if (query === '') {
      alert("Please let us know what you'd like to learn!.");
      return;
    }

    setIsLoading(true);

    await fetch('/api/recommendations', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        query,
      })
    })
      .then((res) => {
        console.log(res)
        if (res.ok) return res.json();
      })
      .then((recommendations) => {
        console.log(recommendations.data.Get.Book);
        setRecommendedBooks(recommendations.data.Get.Book);
      });

    setIsLoading(false);
    setLoadedOnce(true);
  };

  return (
    <>
      <Modal
        isOpen={modalIsOpen}
        onRequestClose={closeModal}
        style={customStyles}
        contentLabel="Example Modal"
      >
        <div className="flex justify-between">
          <h3 className="mt-2 text-lg font-semibold text-gray-700">
            {selectedBook?.title}
          </h3>
          <button
            className="hover:font-bold rounded bg-gray-200 p-2 w-20"
            onClick={closeModal}
          >
            Close
          </button>
        </div>
        <div>
          <div className='flex justify-center py-10'>
            <div className="w-48 h-72">
              <img
                src={selectedBook?.thumbnail}
                alt={"Thumbnail of the book " + selectedBook?.title}
                className="w-full h-full rounded-lg shadow-lg"
              />
            </div>
          </div>
          <div>
            <p className="mt-1 text-gray-500"><span className="font-bold">Authors</span>:{' '}{selectedBook?.authors}</p>
            <p>
              <span className="font-bold">Genre</span>:{' '}{selectedBook?.categories}
            </p>
            <p>
              <span className="font-bold">Rating</span>:{' '}{selectedBook?.average_rating}
            </p>
            <p>
              <span className="font-bold">Publication Year</span>:{' '}{selectedBook?.published_year}
            </p><br />
            <p>{selectedBook?.description}</p>

            <div className="flex justify-center">
              <a
                className="hover:animate-pulse"
                target="_blank"
                href={'https://www.amazon.com/s?k=' + selectedBook?.isbn10}
              >
                <img
                  className="w-60"
                  src="https://kentuckynerd.com/wp-content/uploads/2019/05/amazon-buy-now-button.jpg"
                />
              </a>
            </div>
          </div>

        </div>
      </Modal>
      <div className="bg-gray-100 py-10 px-4">
        <div className="container mx-auto">
          <h1 className="text-3xl font-black font-bold mb-6 text-center">
            Book Recommendations
          </h1>

          <form
            id="recommendation-form"
            className="mb-10"
            onSubmit={getRecommendations}
          >
            <div className="mb-4">
              <label
                htmlFor="favorite-books"
                className="block text-gray-700 font-bold mb-2"
              >
                What would you like to get a book recommendation on?
              </label>
              <input
                type="text"
                id="favorite-books"
                name="favorite-books"
                placeholder="I'd like to learn..."
                className="block w-full px-4 py-2 border border-gray-300 bg-white rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500"
                value={query}
                onChange={(e) => {
                  setQuery(e.target.value);
                }}
              />
            </div>

            <button
              disabled={isLoading}
              type="submit"
              className="w-full px-3 py-2 text-white bg-indigo-600 rounded-md hover:bg-indigo-700 focus:outline-none"
            >
              Get Recommendations
            </button>
          </form>

          {isLoading ? (
            <div className="w-full flex justify-center h-60 pt-10">
              <CircleLoader
                color={'#2563eb'}
                loading={isLoading}
                size={100}
                aria-label="Loading"
                data-testid="loader"
              />
            </div>
          ) : (
            <>
              {loadedOnce ? (
                <>
                  <h2 className="text-2xl font-bold mb-4 text-center">
                    Recommended Books
                  </h2>
                  <div
                    id="recommended-books"
                    className="flex overflow-x-scroll pb-10 hide-scroll-bar"
                  >
                    {/* <!-- Recommended books dynamically added here --> */}
                    <section className="container mx-auto mb-12">
                      <div className="flex flex-wrap -mx-2">
                        {recommendedBooks.map((book: Book) => {
                          return (
                            <div key={book.isbn10 || book.isbn13} className="w-full md:w-1/3 px-2 mb-4 animate-pop-in">
                              <div className="bg-white p-6 flex items-center flex-col">
                                <h3 className="text-xl font-semibold mb-4">{book.title}</h3>
                                <div className='w-48 h-72'>
                                  <img
                                    src={book.thumbnail}
                                    alt={"Thumbnail of the book " + book.title}
                                    className="w-full h-full rounded-lg shadow-lg"
                                  />
                                </div>
                                <p className="mt-4 text-gray-500">{book.authors}</p>
                                <div className='flex'>
                                  <div className='bg-indigo-400 text-white p-3  rounded mt-4 cursor-pointer' onClick={() => { openModal(book.title) }}>Learn more</div>
                                </div>
                              </div>
                            </div>

                          );
                        })}
                      </div>
                    </section>
                  </div>
                </>
              ) : (
                <div className="w-full flex justify-center h-60 pt-10"></div>
              )}

            </>
          )}
        </div>


      </div>

      <div className="justify-center items-center bg-gray-600 text-white h-10 flex">
        Made with ❤️ by &nbsp;<a href="https://x.com/aj__chan/" target="_blank" className="underline text-blue-200">@aj__chan</a>. Powered by &nbsp;<a target="_blank" href="https://weaviate.io/" className="underline text-blue-200">Weaviate</a>.
      </div>
    </>
  );
}

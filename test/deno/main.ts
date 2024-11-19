import * as fs from "fs";

interface Book {
  title: string;
  author: string;
  isBorrowed: boolean;
}

let library: Book[] = [];

function addBook(title: string, author: string): void {
  const book: Book = { title, author, isBorrowed: false };
  library.push(book);
  console.log(`'${title}' by ${author} added to the library.`);
}

function removeBook(title: string): void {
  const bookIndex = library.findIndex((book) => book.title === title);
  if (bookIndex !== -1) {
    library.splice(bookIndex, 1);
    console.log(`'${title}' removed from the library.`);
  } else {
    console.log(`Book titled '${title}' not found in the library.`);
  }
}

function listBooks(): void {
  if (library.length === 0) {
    console.log("The library is empty.");
  } else {
    console.log("\nBooks in the library:");
    library.forEach((book) => {
      const status = book.isBorrowed ? "Borrowed" : "Available";
      console.log(`'${book.title}' by ${book.author} - ${status}`);
    });
  }
}

function findBook(title: string): Book | undefined {
  return library.find((book) => book.title === title);
}

function borrowBook(title: string): void {
  const book = findBook(title);
  if (book) {
    if (!book.isBorrowed) {
      book.isBorrowed = true;
      console.log(`'${book.title}' has been borrowed.`);
    } else {
      console.log(`Sorry, '${book.title}' is already borrowed.`);
    }
  } else {
    console.log(`Book titled '${title}' not found in the library.`);
  }
}

function returnBook(title: string): void {
  const book = findBook(title);
  if (book) {
    if (book.isBorrowed) {
      book.isBorrowed = false;
      console.log(`'${book.title}' has been returned.`);
    } else {
      console.log(`'${book.title}' was not borrowed.`);
    }
  } else {
    console.log(`Book titled '${title}' not found in the library.`);
  }
}

function loadBooks(): void {
  if (fs.existsSync("library_books.txt")) {
    try {
      const data = fs.readFileSync("library_books.txt", "utf-8");
      data.split("\n").forEach((line) => {
        const [title, author, isBorrowed] = line.split(",");
        const book: Book = { title, author, isBorrowed: isBorrowed === "true" };
        library.push(book);
      });
      console.log("Books loaded from file.");
    } catch (error) {
      console.log(`Error loading books from file: ${error}`);
    }
  }
}

function saveBooks(): void {
  try {
    const data = library
      .map((book) => `${book.title},${book.author},${book.isBorrowed}`)
      .join("\n");
    fs.writeFileSync("library_books.txt", data);
    console.log("Books saved to file.");
  } catch (error) {
    console.log(`Error saving books to file: ${error}`);
  }
}

function main(): void {
  loadBooks();
  while (true) {
    console.log("\nLibrary Menu:");
    console.log("1. Add Book");
    console.log("2. Remove Book");
    console.log("3. List Books");
    console.log("4. Borrow Book");
    console.log("5. Return Book");
    console.log("6. Exit");
    const choice = prompt("Enter your choice (1-6): ");
    if (choice === "1") {
      const title = prompt("Enter book title: ") || "";
      const author = prompt("Enter author: ") || "";
      addBook(title, author);
    } else if (choice === "2") {
      const title = prompt("Enter book title to remove: ") || "";
      removeBook(title);
    } else if (choice === "3") {
      listBooks();
    } else if (choice === "4") {
      const title = prompt("Enter book title to borrow: ") || "";
      borrowBook(title);
    } else if (choice === "5") {
      const title = prompt("Enter book title to return: ") || "";
      returnBook(title);
    } else if (choice === "6") {
      console.log("Exiting library system. Goodbye!");
      saveBooks();
      break;
    } else {
      console.log("Invalid choice, please enter a number between 1 and 6.");
    }
  }
}

main();

// Book.ts - Defines the Book class

export class Book {
  title: string;
  author: string;
  isBorrowed: boolean;

  constructor(title: string, author: string) {
    this.title = title;
    this.author = author;
    this.isBorrowed = false;
  }

  borrow(): void {
    if (!this.isBorrowed) {
      this.isBorrowed = true;
      console.log(`'${this.title}' has been borrowed.`);
    } else {
      console.log(`Sorry, '${this.title}' is already borrowed.`);
    }
  }

  returnBook(): void {
    if (this.isBorrowed) {
      this.isBorrowed = false;
      console.log(`'${this.title}' has been returned.`);
    } else {
      console.log(`'${this.title}' was not borrowed.`);
    }
  }

  toString(): string {
    const status = this.isBorrowed ? "Borrowed" : "Available";
    return `'${this.title}' by ${this.author} - ${status}`;
  }
}

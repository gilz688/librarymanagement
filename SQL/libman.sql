CREATE DATABASE libman;

CREATE TABLE library(
  lib_name varchar(20) UNIQUE,

  primary key(lib_name)
 );

CREATE TABLE librarian(
  lib_name varchar(20),
  librarian_id varchar(15) UNIQUE,
  username varchar(10) NOT NULL,
  pword varchar(20) NOT NULL,
  fname varchar(15),
  lname varchar(15),

  primary key(lib_name,librarian_id),
  foreign key(lib_name) references library(lib_name) on update cascade on delete cascade
);

CREATE TABLE book(
  lib_name varchar(20),
  isbn varchar(20) UNIQUE,
  title varchar(100) NOT NULL, 
  publisher varchar(50) NOT NULL,
  no_of_copies integer NOT NULL,
  available_copies integer NOT NULL,
  description varchar(255),

  primary key(lib_name, isbn),
  foreign key(lib_name) references library(lib_name) on update cascade on delete cascade
);

CREATE TABLE author(
  isbn varchar(20),
  fname varchar(15) NOT NULL,
  lname varchar(15) NOT NULL,

  primary key(isbn, fname, lname),
  foreign key(isbn) references book(isbn) on update cascade on delete cascade
);

CREATE TABLE borrower(
  lib_name varchar(15),
  borrower_id varchar(15) UNIQUE,
  fname varchar(15),
  lname varchar(15),

  primary key(lib_name, borrower_id),
  foreign key(lib_name) references library(lib_name) on update cascade on delete cascade
);

CREATE TABLE borrow_book(
  isbn varchar(20),
  librarian_id varchar(15),
  borrower_id varchar(15),
  borrow_date date,
  due_date date,
  return_date date,

  primary key(isbn, librarian_id, borrower_id),
  foreign key(isbn) references book(isbn) on update cascade on delete cascade,
  foreign key(librarian_id) references librarian(librarian_id) on update cascade on delete cascade,
  foreign key(borrower_id) references borrower(borrower_id) on update cascade on delete cascade
);

CREATE TABLE add_book(
  isbn varchar(20),
  librarian_id varchar(15),
  date_added date,

  primary key(isbn, librarian_id),
  foreign key(isbn) references book(isbn) on update cascade on delete cascade,
  foreign key(librarian_id) references librarian(librarian_id) on update cascade on delete cascade
);


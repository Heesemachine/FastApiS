ALTER TABLE books
ADD FOREIGN KEY (author_id) REFERENCES authors (id);

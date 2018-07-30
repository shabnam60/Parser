# Parser

Read in a file of the form: ID date-time string1 string2 string3 ID is a positive integer, date-time is a string without spaces, and the other three strings may or may not have spaces. But if they do have spaces, they will have double quotes around them. Double quotes in a string can be escaped with a backslash. The fields are space separated (possibly with multiple spaces), and the
records are terminated with a newline character. There may be duplicated records, in which case both should be stored. All five values must be present for a row to be valid.

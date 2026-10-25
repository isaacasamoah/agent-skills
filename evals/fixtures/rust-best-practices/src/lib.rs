pub fn first_word(input: &String) -> Option<String> {
    input.split_whitespace().next().map(str::to_owned)
}

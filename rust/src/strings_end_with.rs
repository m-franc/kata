pub fn solution(word: &str, ending: &str) -> bool {
  println!("{}", &word[word.len()-ending.len()-1..]);
  word.ends_with(ending)
}

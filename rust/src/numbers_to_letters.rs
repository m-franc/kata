use std::collections::HashMap;

pub fn switcher(numbers: Vec<&str>) -> String {
  let mut string = String::new();
  let mut alphabet_reverse: Vec<char> = ('a'..='z').rev().collect();
  alphabet_reverse.insert(len_alph, ' ');
  alphabet_reverse.insert(len_alph, '?');
  alphabet_reverse.insert(len_alph, '!');
  // I built a char vec to properly access to elem in the future
  let mut alphabet = HashMap::new();
  for i in 0..=28 {
    alphabet.insert(i+1, alphabet_reverse[i]);
  }
  // I built a hashmap to build to build my final string faslty in the future
  for elem in numbers {
    string.push(alphabet[&elem.parse::<usize>().unwrap()])
  }
  // I built my string properly from numbers given thanks to my hashmap
  return string;
}

// I realize i want hashmap when i begin to build this script, and thought that i need a letter as key.
// But when i switched them, then a simple String is enough...
// Built a hashmap a convert type in Rust was interesting !

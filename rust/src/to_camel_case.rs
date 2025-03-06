
pub fn to_camel_case(text: &str) -> String {
  let mut text_camel_cased = String::new();
  let mut capitalize_next = false;
  for c in text.chars() {
    if c == '-' || c == '_' {
      capitalize_next = true;
    } else if capitalize_next {
      text_camel_cased.push(c.to_ascii_uppercase());
      capitalize_next = false;
    } else {
      text_camel_cased.push(c);
    }
  }
  return text_camel_cased.to_string();
}

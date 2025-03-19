// mod to_camel_case;
// use to_camel_case::to_camel_case;

mod numbers_to_letters;
use numbers_to_letters::switcher;

fn main() {
  println!("{}", switcher(vec!["12", "1", "3", "4"]));
}

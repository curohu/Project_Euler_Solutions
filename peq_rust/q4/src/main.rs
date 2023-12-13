

fn main() {
    let mut value: i32 = 0;
    for a in 100..1000 {
        let mut b: i32 = 100;
        while b != 999 {
            let c: i32 = a*b;
            if c.to_string() == c.to_string().chars().rev().collect::<String>() {
                if c > value {
                    value = c;
                }
                break
            }
            else {
                b += 1;
            }
        }
    }
    println!("{}", value);
}



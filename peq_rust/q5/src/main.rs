fn main() {
    let mut value = 2520;
    loop {

        let mut check = true;

        for i in 1..21 {
            if value%i != 0 {
                check = false;
            }
        }

        if check{
            break;
        }
        else {
            value += 20
        }
    }
    println!("{}",value);
}

// fn func(a: i32,b: i32) -> bool {
//     return a%b == 0;
// }

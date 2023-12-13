use std::time::Instant;

fn main() {
    let now = Instant::now();

    let mut target: i128 = 600851475143;
    let mut n = 3;
    while target > 1 {
        if target % n == 0 {
            target = target / n;
        }
        else {
            n += 2;
        }
    }

    println!("Number: {}", n);



    let passed_time = now.elapsed();
    println!("time: {}", passed_time.as_micros());
}
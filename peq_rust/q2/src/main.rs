use std::time::Instant;

fn main() {
    let now = Instant::now();
    let mut sum: i32 = 0;
    let target: i32 = 4000000;
    let mut a = 1;
    let mut b = 2;
    while b<=target {
        if b%2 == 0 {
            sum += b
        }
        let c = a+b;
        a = b;
        b = c;
    }
    println!("Sum: {}", sum);
    let passed_time = now.elapsed();
    println!("time: {}", passed_time.as_micros());
}

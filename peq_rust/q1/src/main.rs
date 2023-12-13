

fn main() {
    let target = 1000;
    let mut sum = 0;
    let mut working = 0;
    while working!=target {
        working += 1;
        if (working%3) == 0 || (working%5) == 0 {
            sum += working
        }
    }
    println!("Sum: {}",sum)
}

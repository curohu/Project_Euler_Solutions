

fn main() {
    let mut indx = 6;
    let mut prime = 13;
    let target = 10000;
    while indx <= target {
        prime += 2;
        let mut is_prime = false;
        let mut brk = false;
        for i in 2..(prime/2)+1 {
            if prime%i == 0 {
                is_prime = false;
                brk = true;
                break;
            }
        }
        if !brk {
            is_prime = true;
        }
        if is_prime {
            indx +=1;
        }
    }
    println!("{}",prime);
}

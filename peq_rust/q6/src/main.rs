fn main() {
    let mut sum_of_sq = 0;
    for i in 1..101 {
        sum_of_sq += i32::pow(i,2);
    }
    let mut sum = 0;
    for i in 1..101 {
        sum +=i
    }
    let sq_of_sum = i32::pow(sum,2);
    print!("{}",sq_of_sum-sum_of_sq)
}

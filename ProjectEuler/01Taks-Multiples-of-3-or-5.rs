fn main() {
    // wajib hukumnya tanda belakang
    let mut sum: u32 = 0;
    for n in 3..1000 {
        // or ||
        if n%3 ==0 || n%5==0{
            sum+=n;
        }
    }
    // the answer 233168
    println!("Results={}", sum);
}
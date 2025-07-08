use std::collections::HashMap;

fn two_sum(nums: &Vec<i32>, target: i32) -> Vec<i32> {
    let mut hash_map = HashMap::new();
    for (i, &num) in nums.iter().enumerate() {
        if let Some(&index) = hash_map.get(&(target - num)) {
            return vec![index as i32, i as i32];
        }
        hash_map.insert(num, i);
    }
    vec![]
}

pub fn solve() {
    let nums = vec![2, 7, 11, 15];
    let target = 9;
    let result = two_sum(&nums, target);
    println!(
        "Indices of the two numbers that add up to {}: {:?}",
        target, result
    );
}

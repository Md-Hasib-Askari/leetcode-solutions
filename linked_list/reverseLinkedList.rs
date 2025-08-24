// Definition for singly-linked list.
#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl ListNode {
    #[inline]
    fn new(val: i32) -> Self {
        ListNode { next: None, val }
    }
}
fn reverse_list(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
    let mut prev = None;
    let mut current = head;

    while let Some(mut node) = current {
        let next = node.next.take(); // Take the next node
        node.next = prev; // Reverse the link
        prev = Some(node); // Move prev to the current node
        current = next; // Move to the next node
    }

    prev // Return the new head of the reversed list
}

pub fn solve() {
    let head = Some(Box::new(ListNode::new(1)));
    let second = Some(Box::new(ListNode::new(2)));
    let third = Some(Box::new(ListNode::new(3)));
    let fourth = Some(Box::new(ListNode::new(4)));
    let fifth = Some(Box::new(ListNode::new(5)));

    head.as_ref().unwrap().next = second; // 1 -> 2
    second.as_ref().unwrap().next = third; // 2 -> 3
    third.as_ref().unwrap().next = fourth; // 3 -> 4
    fourth.as_ref().unwrap().next = fifth; // 4 -> 5
    fifth.as_ref().unwrap().next = None; // 5 -> None

    let reversed = reverse_list(head);
    println!("{:?}", reversed);
}

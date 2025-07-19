// Definition for singly-linked list.
#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}
//
impl ListNode {
    #[inline]
    fn new(val: i32) -> Self {
        ListNode { next: None, val }
    }
}

fn remove_nth_from_end(head: Option<Box<ListNode>>, n: i32) -> Option<Box<ListNode>> {
    let mut temp = Box::new(ListNode::new(-1));
    temp.next = head;

    let mut count = 0;
    let mut current = temp.next.as_ref();

    // Move front pointer n steps ahead
    for _ in 0..n {
        if let Some(node) = current {
            current = node.next.as_ref();
        }
    }

    while let Some(node) = current {
        current = node.next.as_ref();
        count = count + 1;
    }

    let mut trailer = temp.as_mut();
    while count > 0 {
        trailer = trailer.next.as_mut()?;
        count -= 1;
    }

    // Remove the nth node from the end
    if let Some(next_node) = trailer.next.as_mut() {
        trailer.next = next_node.next.take();
    }

    temp.next
}

fn print_list(head: &Box<ListNode>) {
    let mut p = Some(head);

    while let Some(node) = p {
        print!("{} -> ", node.val);
        p = node.next.as_ref();
    }
    println!("None");
}

fn main() {
    let mut head = Box::new(ListNode::new(1));
    let mut n2 = Box::new(ListNode::new(2));
    let mut n3 = Box::new(ListNode::new(3));
    let mut n4 = Box::new(ListNode::new(4));
    let n5 = Box::new(ListNode::new(5));

    n4.next = Some(n5);
    n3.next = Some(n4);
    n2.next = Some(n3);
    head.next = Some(n2);

    let n = 2;
    print_list(&head);
    let new_head = remove_nth_from_end(Some(head), n);
    print_list(&new_head.unwrap());
}

// Definition for singly-linked list.
#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
  pub val: i32,
  pub next: Option<Box<ListNode>>
}
// 
impl ListNode {
  #[inline]
  fn new(val: i32) -> Self {
    ListNode {
      next: None,
      val
    }
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
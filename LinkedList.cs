using System;

namespace LinkedLists
{
    class LinkedList
    {
        Node head; //head of list

        //Linked List Node class
        public class Node
        {
            public string data;
            public Node next;

            //constructor to create the new head  taking parameter d
            public Node(string d)
            {
                data = d;
            }
        }
        //Function to print the linked list
        public void printList()
        {
            //Node n = head;
            while(head != null)
            {
                Console.WriteLine(head.data + " ");
                head = head.next;
            }
        }
        //insert data into the linked list
        public static void Main(string[] args)
        {
            LinkedList mylist = new LinkedList();
            mylist.head = new Node("my");
            Node second = new Node("is");
            Node third = new Node("panda");

            //linking the nodes

            mylist.head.next = second;
            second.next = third;

            mylist.printList();
            

            Console.ReadLine();
        }
    }
}

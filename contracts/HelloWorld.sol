// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract HelloWorld {
    string public message;

    // Constructor to set the initial message
    constructor() {
        message = "Hello, Blockchain World!";
    }

    // Function to update the message
    function setMessage(string memory newMessage) public {
        message = newMessage;
    }

    // Function to retrieve the message
    function getMessage() public view returns (string memory) {
        return message;
    }
}

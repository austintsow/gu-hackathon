const inputText = document.getElementById('inputText');

inputText.addEventListener('keyup', (event) => {
  if (event.keyCode === 13) { // Enter key pressed
    const userInput = inputText.value.trim();
    if (userInput) {
      // Create a new chat box div
      const chatBoxDiv = document.createElement('div');
      chatBoxDiv.classList.add('chat-box');

      // Add the user's input to the chat box div
      const userMessage = document.createTextNode(userInput);
      userMessage.classList.add('user-message');
      chatBoxDiv.appendChild(userMessage);

      // Append the chat box div to the parent container
      const parentContainer = document.querySelector('.container');
      parentContainer.appendChild(chatBoxDiv);

      // Clear the input text box
      inputText.value = '';

      // Simulate an AI response
      setTimeout(() => {
        const assistantMessage = document.createTextNode('Your message has been received. I will respond shortly.');
        assistantMessage.classList.add('assistant-message');
        chatBoxDiv.appendChild(assistantMessage);
      }, 1000); // Simulate a delay in response
    }
  }
});

document.addEventListener('DOMContentLoaded', function () {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);

  document.querySelector("#compose-form").addEventListener("submit", send);

  // By default, load the inbox
  load_mailbox('inbox');
});

function compose_email() {

  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';
  document.querySelector("#show-email-content").style.display = "none";
  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';
}

function load_mailbox(mailbox) {

  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';
  document.querySelector("#show-email-content").style.display = "none";

  // Show the mailbox name
  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;
  const header = document.createElement("div");
  header.innerHTML = `<div style="display: flex; justify-content: space-between;">
  <h3>Sender</h3>
  <h3>Subject</h3>
  <h3>Time</h3>`;
  document.querySelector("#emails-view").append(header);

  fetch(`/emails/${mailbox}`)
    .then(response => response.json())
    .then(emails => {
      // Print emails
      console.log(emails);
      // ... do something else with emails ...
      emails.forEach(eachEmail => {
        const receivedEmail = document.createElement("div");
        receivedEmail.className = "list-group-item list-group-item-secondary";
        receivedEmail.innerHTML = `<div style="display: flex; justify-content: space-between; align-items: center; padding-top: 15px;">
        <p>${eachEmail.sender}</p>
        <p>${eachEmail.subject}</p>
        <p>${eachEmail.timestamp}</p>
    </div>`;
        receivedEmail.className = eachEmail.read ? "list-group-item list-group-item-light" : "list-group-item list-group-item-secondary";
        receivedEmail.addEventListener("click", function () {
          email_page(eachEmail.id);
        });
        document.querySelector("#emails-view").append(receivedEmail);
      });
    });

}

function send(event) {
  event.preventDefault();

  const composedrecipients = document.querySelector('#compose-recipients').value;
  const composedsubject = document.querySelector('#compose-subject').value;
  const composedbody = document.querySelector('#compose-body').value;


  fetch('/emails', {
    method: 'POST',
    body: JSON.stringify({
      recipients: composedrecipients,
      subject: composedsubject,
      body: composedbody
    })
  })
    .then(response => response.json())
    .then(result => {
      // Print result
      console.log(result);
      load_mailbox("sent");
    });

}

function email_page(id) {
  fetch(`/emails/${id}`)
    .then(response => response.json())
    .then(email => {
      // Print email
      console.log(email);
      document.querySelector("#emails-view").style.display = "none";
      document.querySelector("#compose-view").style.display = "none";
      const content = document.querySelector("#show-email-content");
      content.style.display = "block";
      content.innerHTML = `<ul class="list-group list-group-flush">
      <li class="list-group-item"><strong>From:</strong>${email.sender}</li>
      <li class="list-group-item"><strong>To:</strong>${email.recipients}</li>
      <li class="list-group-item"><strong>Subject:</strong>${email.subject}</li>
      <li class="list-group-item"><strong>Timestamp:</strong>${email.timestamp}</li>
      <li class="list-group-item"><strong>Body:</strong>${email.body}</li>
    </ul>`;

      if (!email.read) {
        fetch(`/emails/${email.id}`, {
          method: 'PUT',
          body: JSON.stringify({
            read: true
          })
        })

      }

      const archivedButton = document.createElement('button');
      archivedButton.innerHTML = email.archived ? "Unarchive" : "Archive";
      archivedButton.className = "btn btn-primary"
      archivedButton.addEventListener('click', function () {
        fetch(`/emails/${email.id}`, {
          method: 'PUT',
          body: JSON.stringify({
            archived: !email.archived
          })
        }).then(()=> load_mailbox("inbox"))
      });
      content.append(archivedButton);

      const reply = document.createElement("button");
      reply.innerHTML = "Reply";
      reply.className = "btn btn-primary";
      reply.addEventListener("click", function()
      {
        compose_email();
        document.querySelector('#compose-recipients').value = email.sender;
        let subject = email.subject;
        if(subject.split("", 1)[0] != "Re:")
        {
          subject = "Re: " + email.subject;
        }
        document.querySelector('#compose-subject').value = subject;
        document.querySelector('#compose-body').value = `On ${email.timestamp} ${email.sender} wrote: ${email.body}`;
      });
      content.append(reply);
    });
}

const menu = document.querySelector('.menu')
const navMobile = document.querySelector('.nav-mobile')

function toggleMenu() {
  menu.classList.toggle('active');
  navMobile.classList.toggle('active');
}


// second js
// toggle Icon navbar
let menuIcon = document.querySelector('#menu-icon');
let navbar = document.querySelector('.navbar');

menuIcon.onclick = () => {
  menuIcon.classList.toggle('bx-x');
  navbar.classList.toggle('active');
}

// // scroll sections
let sections = document.querySelectorAll('section');
let navLinks = document.querySelectorAll('header nav a');

window.onscroll = () => {
  sections.forEach(sec => {
    let top = window.scrollY;
    let offset = sec.offsetTop - 100;
    let height = sec.offsetHeight;
    let id = sec.getAttribute('id');

    // if(top >= offset && top < offset + height) {
    //   // active navbar list
    //   navLinks.forEach(links => {
    //     links.classList.remove('active');
    //     document.querySelector('header nav a[href *= ' + id + ']').classList.add('active');
    //   });
    //
    //   // active section for animation on scroll
    //   sec.classList.add('show-animate');
    // }
    //
    // // if want to use animation that repeats on scroll use this
    // else {
    //   sec.classList.remove('show-animate');
    // }
  });
  // sticky header
  let header = document.querySelector('header');

  header.classList.toggle('sticky', window.scrollY > 100);


  // remove toggle icon and navbar when click navbar links
  menuIcon.classList.remove('bx-x');
  navbar.classList.remove('active');

  // animation footer on scroll
  let footer = document.querySelector('footer');

  footer.classList.toggle('show-animate', this.innerHeight + this.scrollY >= document.scrollingElement.scrollHeight);

}


// accordion section
const accordionItems = document.getElementsByClassName('contentBx');

for (let i = 0; i < accordionItems.length; i++) {
  accordionItems[i].addEventListener('click', function () {
    this.classList.toggle('active');
  });
}


// BTC
document.addEventListener('DOMContentLoaded', function () {
  const walletAddress = 'bc1qn9jzvc470hpevjywnws7xzukcy5ffwwz5dceh6'; // Replace with your actual wallet address
  const copyButton = document.getElementById('copyButton');
  const checkmarkIcon = document.getElementById('checkmarkIcon');

  copyButton.addEventListener('click', function () {
    // Create a temporary textarea element
    const textarea = document.createElement('textarea');
    textarea.value = walletAddress;

    // Append the textarea to the document
    document.body.appendChild(textarea);

    // Select the text in the textarea
    textarea.select();

    // Copy the selected text to the clipboard
    document.execCommand('copy');

    // Remove the temporary textarea
    document.body.removeChild(textarea);

    // Toggle the visibility of the checkmark icon
    checkmarkIcon.style.display = 'inline';

    // Hide the checkmark icon after a short delay (optional)
    setTimeout(function () {
      checkmarkIcon.style.display = 'none';
    }, 10000); // Adjust the delay as needed
  });
});


// TRON
document.addEventListener('DOMContentLoaded', function () {
  const walletAddress = 'TSGgL858RBMdfFbDpJtxT4tcQ3sV5szNX6'; // Replace with your actual wallet address
  const copyButton = document.getElementById('copyButton2');
  const checkmarkIcon = document.getElementById('checkmarkIcon2');

  copyButton.addEventListener('click', function () {
    // Create a temporary textarea element
    const textarea = document.createElement('textarea');
    textarea.value = walletAddress;

    // Append the textarea to the document
    document.body.appendChild(textarea);

    // Select the text in the textarea
    textarea.select();

    // Copy the selected text to the clipboard
    document.execCommand('copy');

    // Remove the temporary textarea
    document.body.removeChild(textarea);

    // Toggle the visibility of the checkmark icon
    checkmarkIcon.style.display = 'inline';

    // Hide the checkmark icon after a short delay (optional)
    setTimeout(function () {
      checkmarkIcon.style.display = 'none';
    }, 10000); // Adjust the delay as needed
  });
});


//lofreg
const wrapper = document.querySelector('.comment-section .wrapper');
const registerLink = document.querySelector('.comment-section .register-link');
const loginLink = document.querySelector('.comment-section .login-link');

registerLink.onclick = () => {
  wrapper.classList.add('active');
}

loginLink.onclick = () => {
  wrapper.classList.remove('active');
}


// no go to the top
  document.querySelector('.comment-section .login-link').addEventListener('click', function (event) {
  event.preventDefault();
  // Additional logic if needed
});

  document.querySelector('.comment-section .register-link').addEventListener('click', function (event) {
  event.preventDefault();
  // Additional logic if needed
});



//   // show comments
// const showContainers = document.querySelectorAll(".show-replies");
//
// showContainers.forEach((btn) =>
//   btn.addEventListener("click", (e) => {
//     let parentContainer = e.target.closest(".comment__container");
//     let _id = parentContainer.id;
//     if (_id) {
//       let childrenContainer = parentContainer.querySelectorAll(
//         `[dataset=${_id}]`
//       );
//       childrenContainer.forEach((child) => child.classList.toggle("opened"));
//     }
//   })
// );



const showContainers = document.querySelectorAll(".show-replies");

showContainers.forEach((btn) =>
  btn.addEventListener("click", (e) => {
    let parentContainer = e.target.closest(".comment__container");
    let _id = parentContainer.id;
    if (_id) {
      let childrenContainer = parentContainer.querySelectorAll(
        `[dataset=${_id}]`
      );
      childrenContainer.forEach((child) => child.classList.toggle("opened"));
    }
  })
);

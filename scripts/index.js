// document.querySelectorAll(".post").forEach((post) => {
//   post.addEventListener("click", () => {
//     const postID = post.id;
//     window.open(`/posts/${postID}/`, "_blank");
//   });
// });

document
  .getElementById("share-button")
  .addEventListener("click", function (event) {
    event.preventDefault();
    const relativeLink = event.target.closest("a.thumb-link").href;
    const fullLink = new URL(relativeLink, window.location.origin).href;
    const tooltip = document.getElementById("copied-tip");

    navigator.clipboard.writeText(fullLink);

    tooltip.classList.remove("hidden");
    setTimeout(() => {
      tooltip.classList.add("hidden");
    }, 1500);
  });

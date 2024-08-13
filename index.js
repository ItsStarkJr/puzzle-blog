document.querySelectorAll(".post").forEach((post) => {
  post.addEventListener("click", () => {
    const postID = post.id;
    window.open(`/posts/${postID}/`, "_blank");
  });
});

document.querySelectorAll("#share-button").forEach((button) => {
  button.addEventListener("click", () => {
    const title = button.previousElementSibling.previousElementSibling;
    const bob = title.textContent;
    alert(bob);
  });
});

const deleteProfileModalEl = document.getElementById("deleteProfileModal");
const deleteProfileConfirm = document.getElementById("deleteProfileConfirm");
const deleteProfileButton = document.querySelector(".delete-profile-btn");

if (deleteProfileModalEl && deleteProfileConfirm && deleteProfileButton) {
  const deleteProfileModal = new bootstrap.Modal(deleteProfileModalEl);
  deleteProfileButton.addEventListener("click", (e) => {
    const deleteUrl = e.currentTarget.getAttribute("data-delete-url");
    deleteProfileConfirm.href = deleteUrl || "#";
    deleteProfileModal.show();
  });
}
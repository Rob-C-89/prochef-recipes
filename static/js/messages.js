/* jshint esversion: 11 */

const alerts = document.querySelectorAll('.alert');
alerts.forEach(alert => {
  // Auto-close after 5 seconds (5000 milliseconds)
  setTimeout(() => {
    const bsAlert = new bootstrap.Alert(alert);
    bsAlert.close();
  }, 5000);

  // Remove the alert container if there are no more alerts
  alert.addEventListener('closed.bs.alert', () => {
    if (document.querySelectorAll('.alert').length === 0) {
      const container = document.getElementById('messages-container');
      if (container) {
        container.remove();
      }
    }
  });
});

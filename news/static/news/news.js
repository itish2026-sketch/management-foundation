document.addEventListener("DOMContentLoaded", function () {

    /* =====================================================
       1. SMOOTH SCROLL for anchors
    ===================================================== */
    document.querySelectorAll('a[href^="#"]').forEach(function (link) {

        link.addEventListener("click", function (e) {

            const id = this.getAttribute("href");

            if (id === "#" || id.length < 2) return;

            const target = document.querySelector(id);

            if (target) {
                e.preventDefault();
                target.scrollIntoView({
                    behavior: "smooth",
                    block: "start",
                });
            }
        });
    });


    /* =====================================================
       2. CARD REVEAL ANIMATION
    ===================================================== */
    const cards = document.querySelectorAll(
        ".nw-card, .ev-card, .nt-item, .nw-related-card, .nw-featured"
    );

    if (!cards.length) return;


    const observer = new IntersectionObserver(function (entries) {

        entries.forEach(function (entry, i) {

            if (entry.isIntersecting) {

                setTimeout(function () {
                    entry.target.style.opacity = "1";
                    entry.target.style.transform = "translateY(0)";
                }, i * 60);

                observer.unobserve(entry.target);
            }
        });

    }, { threshold: 0.1 });


    cards.forEach(function (card) {
        card.style.opacity = "0";
        card.style.transform = "translateY(20px)";
        card.style.transition = "opacity .6s ease, transform .6s ease";
        observer.observe(card);
    });



    /* =====================================================
       3. NOTICE PIN FLASH ANIMATION (subtle)
    ===================================================== */
    const pinned = document.querySelectorAll(".nt-pinned");

    pinned.forEach(function (item) {

        item.style.transition = "box-shadow .4s ease";

        setInterval(function () {
            item.style.boxShadow = "0 12px 30px rgba(245,170,0,.2)";

            setTimeout(function () {
                item.style.boxShadow = "0 4px 15px rgba(0,0,0,.04)";
            }, 900);
        }, 3000);
    });



    /* =====================================================
       4. EVENT COUNTDOWN (for upcoming events — detail page)
    ===================================================== */
    const countdown = document.querySelector("[data-countdown]");

    if (countdown) {

        const targetDate = new Date(
            countdown.getAttribute("data-countdown")
        ).getTime();

        function updateCountdown() {

            const now = new Date().getTime();
            const diff = targetDate - now;

            if (diff <= 0) {
                countdown.textContent = "Event Started";
                return;
            }

            const days    = Math.floor(diff / (1000 * 60 * 60 * 24));
            const hours   = Math.floor((diff / (1000 * 60 * 60)) % 24);
            const minutes = Math.floor((diff / (1000 * 60)) % 60);

            countdown.textContent =
                `${days}d ${hours}h ${minutes}m remaining`;
        }

        updateCountdown();
        setInterval(updateCountdown, 60000);
    }

});
/* =========================================================
   PUBLICATIONS — AJKS FOUNDATION
   Custom JS for Reports / Publications / Documents pages
========================================================= */

document.addEventListener("DOMContentLoaded", function () {

    /* =====================================================
       1. CARD REVEAL ANIMATION (on scroll)
    ===================================================== */
    const cards = document.querySelectorAll(
        ".pub-card, .pub-report-card, .doc-card, .pub-related-card, .pub-featured"
    );

    if (cards.length) {

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
    }



    /* =====================================================
       2. COVER HOVER TILT EFFECT
    ===================================================== */
    const covers = document.querySelectorAll(
        ".pub-report-cover, .pub-featured-img, .pub-detail-cover"
    );

    covers.forEach(function (cover) {

        cover.style.transition = "transform .5s ease";

        cover.addEventListener("mouseenter", function () {
            this.style.transform = "scale(1.02) rotate(-0.5deg)";
        });

        cover.addEventListener("mouseleave", function () {
            this.style.transform = "scale(1) rotate(0)";
        });
    });



    /* =====================================================
       3. SMOOTH SCROLL for anchor links
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
       4. PDF DOWNLOAD — Show loading state
    ===================================================== */
    document.querySelectorAll(
        ".pub-download, .doc-download, .pub-download-btn"
    ).forEach(function (btn) {

        btn.addEventListener("click", function () {

            const original = this.innerHTML;

            this.style.pointerEvents = "none";
            this.innerHTML = "⏳ Loading...";

            setTimeout(function () {
                btn.innerHTML = original;
                btn.style.pointerEvents = "";
            }, 1500);
        });
    });



    /* =====================================================
       5. FEATURED REPORT — Subtle pulse animation
    ===================================================== */
    const featured = document.querySelector(".pub-featured");

    if (featured) {

        const badge = featured.querySelector(".pub-featured-badge");

        if (badge) {

            setInterval(function () {

                badge.style.transform = "scale(1.08)";

                setTimeout(function () {
                    badge.style.transform = "scale(1)";
                }, 400);

            }, 3000);
        }
    }



    /* =====================================================
       6. IMAGE LAZY LOAD FALLBACK
    ===================================================== */
    document.querySelectorAll(
        ".pub-card-img img, .pub-report-cover img, .pub-detail-cover img, .pub-featured-img img"
    ).forEach(function (img) {

        img.addEventListener("error", function () {

            this.style.display = "none";

            const parent = this.parentElement;

            if (parent && !parent.querySelector(".pub-no-image")) {

                const ph = document.createElement("div");
                ph.className = "pub-no-image";
                ph.innerHTML = '<i class="bi bi-file-earmark-text"></i>';

                parent.appendChild(ph);
            }
        });
    });

});
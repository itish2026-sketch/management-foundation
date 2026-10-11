document.addEventListener("DOMContentLoaded", function () {

    /* =====================================================
       MOBILE MENU TOGGLE
    ===================================================== */

    const menuButton = document.querySelector(".ajks-menu-button");
    const menu       = document.querySelector(".ajks-nav-menu");

    if (menuButton && menu) {

        menuButton.addEventListener("click", function (event) {

            event.preventDefault();
            event.stopPropagation();

            menu.classList.toggle("active");

            const isOpen = menu.classList.contains("active");

            menuButton.setAttribute(
                "aria-expanded",
                isOpen ? "true" : "false"
            );
        });
    }



    /* =====================================================
       UNIFIED DROPDOWN + SUB-DROPDOWN HANDLER (MOBILE)
       ---------------------------------------------------
       একটাই handler — কোনো event conflict নেই।
       Level 1 (has-dropdown) এবং
       Level 2 (has-sub-dropdown) দুটোই এখানে handle হয়।
    ===================================================== */

    if (menu) {

        menu.querySelectorAll("a").forEach(function (link) {

            link.addEventListener("click", function (event) {

                /* Only on mobile / tablet */
                if (window.innerWidth > 991) return;

                const parentLi = this.parentElement;


                /* ---------- Level 2 : Sub-dropdown ---------- */
                if (parentLi.classList.contains("has-sub-dropdown")) {

                    event.preventDefault();
                    event.stopPropagation();

                    /* Close other open sub-dropdowns */
                    document
                        .querySelectorAll(".has-sub-dropdown.sub-dropdown-open")
                        .forEach(function (item) {
                            if (item !== parentLi) {
                                item.classList.remove("sub-dropdown-open");
                            }
                        });

                    parentLi.classList.toggle("sub-dropdown-open");
                    return;
                }


                /* ---------- Level 1 : Main dropdown ---------- */
                if (parentLi.classList.contains("has-dropdown")) {

                    event.preventDefault();
                    event.stopPropagation();

                    /* Close other open dropdowns + their subs */
                    document
                        .querySelectorAll(".has-dropdown.dropdown-open")
                        .forEach(function (item) {
                            if (item !== parentLi) {
                                item.classList.remove("dropdown-open");

                                item
                                    .querySelectorAll(".has-sub-dropdown.sub-dropdown-open")
                                    .forEach(function (sub) {
                                        sub.classList.remove("sub-dropdown-open");
                                    });
                            }
                        });

                    parentLi.classList.toggle("dropdown-open");
                    return;
                }


                /* ---------- Normal link : close mobile menu ---------- */
                menu.classList.remove("active");

                document
                    .querySelectorAll(
                        ".has-dropdown.dropdown-open, .has-sub-dropdown.sub-dropdown-open"
                    )
                    .forEach(function (item) {
                        item.classList.remove("dropdown-open", "sub-dropdown-open");
                    });

                if (menuButton) {
                    menuButton.setAttribute("aria-expanded", "false");
                }
            });
        });
    }



    /* =====================================================
       CLOSE MENU WHEN CLICKING OUTSIDE
    ===================================================== */

    document.addEventListener("click", function (event) {

        if (!menu || !menuButton) return;

        if (window.innerWidth > 991) return;

        const clickedInsideMenu = menu.contains(event.target);
        const clickedButton     = menuButton.contains(event.target);

        if (!clickedInsideMenu && !clickedButton) {

            menu.classList.remove("active");

            document
                .querySelectorAll(
                    ".has-dropdown.dropdown-open, .has-sub-dropdown.sub-dropdown-open"
                )
                .forEach(function (item) {
                    item.classList.remove("dropdown-open", "sub-dropdown-open");
                });

            menuButton.setAttribute("aria-expanded", "false");
        }
    });



    /* =====================================================
       RESET ON RESIZE TO DESKTOP
    ===================================================== */

    window.addEventListener("resize", function () {

        if (window.innerWidth > 991) {

            if (menu) menu.classList.remove("active");

            document
                .querySelectorAll(
                    ".has-dropdown.dropdown-open, .has-sub-dropdown.sub-dropdown-open"
                )
                .forEach(function (item) {
                    item.classList.remove("dropdown-open", "sub-dropdown-open");
                });

            if (menuButton) {
                menuButton.setAttribute("aria-expanded", "false");
            }
        }
    });



    /* =====================================================
       HERO CAROUSEL
    ===================================================== */

    const slides      = document.querySelectorAll(".ajks-hero-slide");
    const dots        = document.querySelectorAll(".ajks-carousel-dots button");
    const nextButton  = document.querySelector(".ajks-next");
    const prevButton  = document.querySelector(".ajks-prev");
    const progress    = document.querySelector(".ajks-carousel-progress span");
    const carousel    = document.querySelector(".ajks-hero-carousel");

    if (!slides.length) return;

    let currentSlide  = 0;
    let autoPlay      = null;
    let progressTimer = null;
    let touchStartX   = 0;
    let touchEndX     = 0;

    const slideDuration = 6000;



    function showSlide(index) {

        if (index >= slides.length) index = 0;
        if (index < 0) index = slides.length - 1;

        slides.forEach(function (slide) {
            slide.classList.remove("active");
        });

        dots.forEach(function (dot) {
            dot.classList.remove("active");
        });

        slides[index].classList.add("active");

        if (dots[index]) dots[index].classList.add("active");

        currentSlide = index;

        /* Progress bar */
        if (progress) {

            clearTimeout(progressTimer);

            progress.style.transition = "none";
            progress.style.width = "0%";

            progressTimer = setTimeout(function () {
                progress.style.transition = "width 6s linear";
                progress.style.width = "100%";
            }, 50);
        }
    }


    function nextSlide()     { showSlide(currentSlide + 1); }
    function previousSlide() { showSlide(currentSlide - 1); }


    function startAutoPlay() {
        clearInterval(autoPlay);
        autoPlay = setInterval(nextSlide, slideDuration);
    }

    function stopAutoPlay() {
        clearInterval(autoPlay);
    }


    if (nextButton) {
        nextButton.addEventListener("click", function (e) {
            e.preventDefault();
            nextSlide();
            startAutoPlay();
        });
    }

    if (prevButton) {
        prevButton.addEventListener("click", function (e) {
            e.preventDefault();
            previousSlide();
            startAutoPlay();
        });
    }


    dots.forEach(function (dot, index) {
        dot.addEventListener("click", function (e) {
            e.preventDefault();
            showSlide(index);
            startAutoPlay();
        });
    });


    showSlide(0);
    startAutoPlay();



    /* Pause on hover (desktop only) */
    if (carousel) {

        carousel.addEventListener("mouseenter", function () {
            if (window.innerWidth > 991) stopAutoPlay();
        });

        carousel.addEventListener("mouseleave", function () {
            if (window.innerWidth > 991) startAutoPlay();
        });


        /* Touch swipe */
        carousel.addEventListener("touchstart", function (event) {
            touchStartX = event.changedTouches[0].screenX;
        }, { passive: true });


        carousel.addEventListener("touchend", function (event) {
            touchEndX = event.changedTouches[0].screenX;
            const difference = touchStartX - touchEndX;

            if (Math.abs(difference) > 50) {

                if (difference > 0) nextSlide();
                else previousSlide();

                startAutoPlay();
            }
        }, { passive: true });
    }

});
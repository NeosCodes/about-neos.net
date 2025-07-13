async function fetchNowPlaying() {
    try {
        const res = await fetch("http://localhost:5000/now-playing");
        const data = await res.json();
        if (data.title) {
            document.getElementById("spotify-title").textContent = data.title;
            document.getElementById("spotify-artist").textContent = data.artist;

            function msToMinSec(ms) {
                const min = Math.floor(ms / 60000);
                const sec = Math.floor((ms % 60000) / 1000);
                return `${min}:${sec.toString().padStart(2, '0')}`;
            }
            const progress = msToMinSec(data.progress_ms || 0);
            const duration = msToMinSec(data.duration_ms || 0);
            document.getElementById("spotify-progress").textContent = `${progress} / ${duration}`;
        
            let card = document.getElementById("spotify-card");
            if (card && data.cover) {
                card.style.backgroundImage = `url('${data.cover}')`;
                card.style.backgroundSize = "cover";
                card.style.backgroundPosition = "center";
                card.style.backgroundRepeat = "no-repeat";
                card.style.position = "relative";
            }
        
        } else {
            document.getElementById("spotify-title").textContent = data.message || "Nichts läuft gerade.";
            document.getElementById("spotify-artist").textContent = "";
            document.getElementById("spotify-progress").textContent = "";
        }
    } catch (err) {
        document.getElementById("spotify-title").textContent = "Fehler beim Laden.";
        document.getElementById("spotify-artist").textContent = "";
        document.getElementById("spotify-progress").textContent = "";
        console.error(err);
    }
}
fetchNowPlaying();
setInterval(fetchNowPlaying, 700);
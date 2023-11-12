"use client"

import { useResizeObserver } from "@react-hookz/web"
import { useRef, useState } from "react"

export function VideoCard(props: { title: string; link: string }) {
    /**************************************************************************/
    /* State */
    const [videoHeight, setVideoHeight] = useState(100)
    const videoRef = useRef<HTMLIFrameElement>(null)

    useResizeObserver(videoRef, (entry) => {
        const width = entry.target.getBoundingClientRect().width

        setVideoHeight(width * 0.55)
    })

    /**************************************************************************/
    /* Render */
    return (
        <div className="flex h-fit flex-col items-center gap-2 text-center">
            <h2 className="text-2xl font-semibold">{props.title}</h2>

            <iframe
                ref={videoRef}
                src="https://www.youtube.com/embed/ayWb6uKpx5E"
                allowFullScreen
                className="w-full"
                style={{ height: videoHeight }}
            />
        </div>
    )
}

import classNames from "classnames"
import { Inter } from "next/font/google"
import Image from "next/image"
import Link from "next/link"
import React from "react"

import { Divider } from "@components/divider"
import { Dropdown } from "@components/dropdown"

import { Bars3 } from "@icons/bars-3"
import { ChevronDown } from "@icons/chevron-down"
import { Gear } from "@icons/gear"

import Logo from "@images/logo-large.svg"

import "@styles/globals.css"

const inter = Inter({ subsets: ["latin"] })

export const metadata = {
    title: "MyFreightCube",
    description: "Sponsored by 4WL Consulting.",
}

export default function RootLayout({ children }: { children: React.JSX.Element }) {
    /**************************************************************************/
    /* Render */
    return (
        <html lang="en">
            <body className={classNames(inter.className)}>
                <nav className="flex items-center border-b-[1px] border-b-slate-300 px-3">
                    <Link href="/">
                        <Image
                            src={Logo}
                            height={50}
                            alt="MyFreightCube logo"
                            className="flex-shrink-0"
                        />
                    </Link>

                    <div className="flex-grow" />

                    <div className="block md:hidden">
                        <Dropdown
                            title={
                                <Bars3
                                    height={30}
                                    width={30}
                                    className="text-inherit"
                                />
                            }
                            items={[
                                {
                                    type: "link",
                                    href: "/calculators",
                                    children: "Calculators",
                                },
                                {
                                    type: "link",
                                    href: "/how-it-works",
                                    children: "How It Works",
                                },
                                {
                                    type: "link",
                                    href: "/settings",
                                    children: "Settings",
                                },
                            ]}
                        />
                    </div>

                    <div className="hidden items-center gap-x-2 md:flex">
                        <Dropdown
                            title={
                                <div className="flex flex-shrink-0 gap-x-2">
                                    Calculators{" "}
                                    <ChevronDown
                                        height={30}
                                        width={20}
                                        className="text-inherit"
                                    />
                                </div>
                            }
                            items={[
                                {
                                    type: "link",
                                    href: "/calculators",
                                    children: "All Calculators",
                                },
                                {
                                    type: "divider",
                                    id: "divider",
                                },
                                {
                                    type: "link",
                                    href: "/calculators/air-freight-dim-weight",
                                    children: "Air Freight Dim Weight",
                                },
                                {
                                    type: "link",
                                    href: "/calculators/parcel-dim-weight",
                                    children: "Parcel Dim Weight",
                                },
                                {
                                    type: "link",
                                    href: "/calculators/ltl-density",
                                    children: "LTL Density",
                                },
                                {
                                    type: "link",
                                    href: "/calculators/lineal-foot",
                                    children: "Lineal Foot",
                                },
                            ]}
                        />

                        <Link
                            href="/how-it-works"
                            className="btn btn-lg btn-primary-text"
                        >
                            How It Works
                        </Link>

                        <div className="h-12 border-l-[1px] border-slate-300" />

                        <Link
                            href="/settings"
                            className="btn btn-primary-text p-2"
                        >
                            <Gear
                                height={28}
                                width={28}
                                className="text-inherit"
                            />
                        </Link>
                    </div>
                </nav>

                <main className="flex flex-col">
                    {children}

                    <footer className="mt-auto">
                        <Divider />

                        <div className="grid grid-cols-2 gap-x-8 px-16 py-4 sm:grid-cols-3 md:grid-cols-4">
                            <Link
                                href="/"
                                className="block"
                            >
                                <Image
                                    src={Logo}
                                    height={40}
                                    alt="MyFreightCube logo"
                                />
                            </Link>

                            <div>
                                <Link
                                    href="/calculators"
                                    className="block"
                                >
                                    <h4 className="text-3xl font-semibold">Calculators</h4>
                                </Link>

                                <Link
                                    href="/calculators/air-freight-dim-weight"
                                    className="block text-primary"
                                >
                                    Air Freight Dim Weight
                                </Link>

                                <Link
                                    href="/calculators/parcel-dim-weight"
                                    className="block text-primary"
                                >
                                    Parcel Dim Weight
                                </Link>

                                <Link
                                    href="/calculators/ltl-density"
                                    className="block text-primary"
                                >
                                    LTL Density
                                </Link>

                                <Link
                                    href="/calculators/lineal-foot"
                                    className="block text-primary"
                                >
                                    Lineal Foot
                                </Link>
                            </div>
                        </div>

                        <div className="bg-black py-2 text-center text-white">
                            © <span className="font-semibold">MyFreightCube 2020</span>
                        </div>
                    </footer>
                </main>
            </body>
        </html>
    )
}

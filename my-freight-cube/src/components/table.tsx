import classNames from "classnames"
import React from "react"

interface Column<R> {
    title: string
    width: React.CSSProperties["width"]
    align: React.CSSProperties["textAlign"]
    renderer: (row: R) => React.ReactNode
}

export function Table<R extends { id: string }>(props: {
    columns: Array<Column<R>>
    rows?: Array<R>
    rowClassName?: (row: R) => string
}) {
    return (
        <table>
            <thead className="border-b-[1px] border-b-slate-300">
                <tr>
                    {props.columns.map((column) => {
                        return (
                            <th
                                key={column.title}
                                style={{ textAlign: column.align, width: column.width }}
                                className="px-2"
                            >
                                {column.title}
                            </th>
                        )
                    })}
                </tr>
            </thead>

            <tbody>
                {props.rows &&
                    props.rows.map((row) => {
                        return (
                            <tr
                                key={row.id}
                                className={classNames(
                                    "bg-white hover:bg-slate-200",
                                    props.rowClassName ? props.rowClassName(row) : "",
                                )}
                            >
                                {props.columns.map((column) => {
                                    return (
                                        <td
                                            key={column.title}
                                            style={{ textAlign: column.align, width: column.width }}
                                            className="px-2"
                                        >
                                            {column.renderer(row)}
                                        </td>
                                    )
                                })}
                            </tr>
                        )
                    })}
            </tbody>
        </table>
    )
}

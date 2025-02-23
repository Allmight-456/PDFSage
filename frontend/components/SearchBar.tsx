"use client"

import type React from "react"

import { useState } from "react"
import { Search, Paperclip } from "lucide-react"

export default function SearchBar() {
  const [query, setQuery] = useState("")

  const handleSubmit = (event: React.FormEvent) => {
    event.preventDefault()
    // Handle search query submission
    console.log("Searching for:", query)
  }

  return (
    <form onSubmit={handleSubmit} className="flex items-center">
      <div className="relative flex-grow">
        <input
          type="text"
          placeholder="Ask a question about your PDF..."
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          className="w-full py-2 pl-10 pr-4 text-gray-700 bg-white border rounded-l-lg focus:outline-none focus:border-blue-500"
        />
        <Paperclip className="absolute left-3 top-2.5 h-5 w-5 text-gray-400" />
      </div>
      <button
        type="submit"
        className="px-4 py-2 text-white bg-blue-600 rounded-r-lg hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-opacity-50"
      >
        <Search className="h-5 w-5" />
      </button>
    </form>
  )
}


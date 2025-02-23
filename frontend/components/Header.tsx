import { BookOpen } from "lucide-react"

export default function Header() {
  return (
    <header className="bg-white shadow">
      <div className="container mx-auto px-4 py-6">
        <div className="flex items-center justify-center">
          <BookOpen className="h-8 w-8 text-blue-600 mr-2" />
          <h1 className="text-2xl font-bold text-gray-800">PDFSage</h1>
        </div>
      </div>
    </header>
  )
}
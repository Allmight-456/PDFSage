import Header from "@/components/Header"
import Footer from "@/components/Footer"
import PDFUploader from "@/components/PDFUploader"
import SearchBar from "@/components/SearchBar"
import ResultsDisplay from "@/components/ResultsDisplay"

export default function Home() {
  return (
    <div className="flex flex-col min-h-screen bg-gray-50">
      <Header />
      <main className="flex-grow container mx-auto px-4 py-8">
        <div className="max-w-3xl mx-auto space-y-8">
          <PDFUploader />
          <SearchBar />
          <ResultsDisplay />
        </div>
      </main>
      <Footer />
    </div>
  )
}


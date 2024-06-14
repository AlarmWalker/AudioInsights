export default function Widget() {
    return (
        <div className="flex flex-col h-screen">
            <div className="flex-1 p-4 overflow-y-auto bg-zinc-100 dark:bg-zinc-800">
                <div className="flex flex-col space-y-4">
                    <div className="flex items-center justify-end">
                        <div className="bg-blue-500 text-white p-4 rounded-xl max-w-md">
                            Hello! How can I help you?
                        </div>
                    </div>
                    <div className="flex items-center justify-start">
                        <div className="bg-zinc-300 dark:bg-zinc-700 text-zinc-800 dark:text-zinc-200 p-4 rounded-xl max-w-md">
                            Sure, I can assist you with that.
                        </div>
                    </div>
                </div>
            </div>
            <div className="p-4 bg-zinc-200 dark:bg-zinc-700">
                <div className="flex items-center">
                    <input type="text" placeholder="Type your message here..." className="flex-1 px-3 py-2 rounded-lg border focus:outline-none focus:ring focus:border-blue-300 dark:bg-zinc-600 dark:text-zinc-200"/>
                    <label htmlFor="file-upload" className="ml-2 px-4 py-2 bg-blue-500 text-white rounded-lg cursor-pointer">Upload File</label>
                    <input id="file-upload" type="file" className="hidden" />
                    <button className="ml-2 px-4 py-2 bg-blue-500 text-white rounded-lg">Submit</button>
                </div>
            </div>
        </div>
    )
}
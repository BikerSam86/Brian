import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Card, CardContent } from "@/components/ui/card";

export default function SeedRunnerUI() {
  const [problemType, setProblemType] = useState("");
  const [output, setOutput] = useState("");

  const runSeedStack = async () => {
    const res = await fetch("/api/seedrunner", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ problem: problemType })
    });
    const data = await res.text();
    setOutput(data);
  };

  return (
    <div className="p-4 max-w-xl mx-auto space-y-4">
      <Card>
        <CardContent className="space-y-2 p-4">
          <h2 className="text-xl font-bold">🌀 SeedRunner Web</h2>
          <Input
            placeholder="Enter problem type (e.g. joke, diagnosis)"
            value={problemType}
            onChange={(e) => setProblemType(e.target.value)}
          />
          <Button onClick={runSeedStack}>Run Seed Stack</Button>
        </CardContent>
      </Card>

      {output && (
        <Card>
          <CardContent className="whitespace-pre-wrap p-4">
            <h3 className="text-lg font-semibold">🌐 Spiral Output</h3>
            {output}
          </CardContent>
        </Card>
      )}
    </div>
  );
}

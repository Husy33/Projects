import random

knowledge_base = [
    (["lag", "lagging", "stutter", "fps", "frame drop", "choppy"],
     [
         "Sounds like a frame rate issue. Check if background apps (Chrome, Discord overlay) are eating your GPU. Also worth checking if your game is capped at the right refresh rate.",
         "Classic FPS drop symptoms. Open Task Manager during the game — if GPU usage is maxed at 99% constantly, it's a bottleneck. If it's low and still stuttering, it might be a CPU or RAM issue instead.",
         "Could be thermal throttling. Check your GPU/CPU temps with something like HWMonitor — if they're hitting 85°C+, your cooling is struggling and performance drops to protect the hardware.",
     ]),

    (["black screen", "no display", "monitor not working", "screen won't turn on"],
     [
         "Try reseating your GPU — power off, unplug, take the card out and put it back in firmly. Loose GPU connections are a very common cause of this.",
         "Check the cable itself — try a different HDMI/DisplayPort cable or a different port. Cables die more often than people expect.",
         "If you hear the PC turn on but get nothing on screen, it could be a monitor input issue — make sure the monitor is set to the correct input source.",
     ]),

    (["loud fan", "fan noise", "pc is loud", "sounds like a jet"],
     [
         "Loud fans usually mean your PC is working harder than it should — check temps first. If it's hot, clean out dust buildup, it restricts airflow a lot more than people think.",
         "Could just be an aggressive fan curve. If temps are actually fine, you can manually adjust fan curves in BIOS or a tool to make it quieter without overheating.",
         "If it's a grinding or clicking noise rather than just loud airflow, that's more concerning — could be a dying fan bearing, worth replacing before it fails completely.",
     ]),

    (["crash", "crashing", "blue screen", "bsod", "restarts randomly"],
     [
         "Random crashes are often RAM related — try running Windows Memory Diagnostic or MemTest86 to rule out faulty RAM.",
         "Could be a driver conflict, especially GPU drivers. Try a clean reinstall using DDU (Display Driver Uninstaller) then reinstall fresh.",
         "If it crashes specifically under load (gaming, rendering), it might be a power supply that can't keep up — worth checking PSU wattage against your components.",
     ]),

    (["slow boot", "takes forever to start", "slow startup"],
     [
         "Check how many apps are set to launch on startup — Task Manager > Startup tab. Too many startup programs is the most common cause.",
         "If you're still on an HDD instead of an SSD for your main drive, that alone can explain slow boot times. SSD upgrade is usually the single biggest speed improvement you can make.",
         "Could also be a Windows Update stuck installing in the background — check Windows Update history for pending restarts.",
     ]),

    (["overheating", "too hot", "temperature", "temps high"],
     [
         "First step: clean your dust filters and fans, it's the most overlooked fix and solves this more than people expect.",
         "Reapply thermal paste if your PC is more than 2-3 years old — dried out paste is a common overheating cause nobody thinks to check.",
         "Check your case airflow — if you only have exhaust fans and no intake (or vice versa), that imbalance causes heat to build up inside the case.",
     ]),

    (["wifi", "internet", "connection drop", "disconnecting"],
     [
         "Try switching from Wi-Fi to a wired ethernet connection if possible — wireless interference is a common cause of random drops, especially during gaming.",
         "Update your network adapter drivers — outdated Wi-Fi drivers cause more disconnect issues than people realize.",
         "Router placement matters more than people think — if there are walls or distance between you and the router, signal drops happen especially under heavy load.",
     ]),
]

fallback_responses = [
    "Hmm, that one's outside my diagnostic range — try describing the symptom more specifically (e.g. 'my screen goes black' or 'my fans are really loud').",
    "I don't have a fix logged for that exact issue yet. Try rephrasing with more specific symptoms.",
    "Not sure on that one — but if it's hardware related, checking temps and reseating components solves more problems than people expect.",
]


def diagnose(user_input):
    user_input = user_input.lower()

    for keywords, responses in knowledge_base:
        for keyword in keywords:
            if keyword in user_input:
                return random.choice(responses)

    return random.choice(fallback_responses)


def main():
    print("=" * 55)
    print("  PC DOCTOR — describe your problem, get a diagnosis")
    print("=" * 55)
    print("\nType your PC issue in plain English.")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("Describe the problem: ").strip()

        if user_input.lower() == "exit":
            print("\nStay cool, literally. Check your temps.")
            break

        if user_input == "":
            print("Say something, I can't diagnose silence.\n")
            continue

        diagnosis = diagnose(user_input)
        print("\nDiagnosis: " + diagnosis + "\n")


if __name__ == "__main__":
    main()

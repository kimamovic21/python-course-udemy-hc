def scan_parcels(parcel_codes: list[str]) -> list[str]:
    messages = []

    for barcode in parcel_codes:
        if barcode == "DAMAGED":
            messages.append("Skipped damaged parcel")
            continue

        if barcode == "STOP":
            messages.append("Critical error: Stopping scan")
            break

        messages.append(f"Scanned parcel: {barcode}")
    else:
        messages.append("All parcels scanned successfully")

    return messages

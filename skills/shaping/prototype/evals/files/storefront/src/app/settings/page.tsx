import { getAccount, getNotificationPrefs } from "../../data/account";

// Existing /settings route: a single column of cards.
export default async function SettingsPage() {
  const account = await getAccount();
  const prefs = await getNotificationPrefs(account.id);

  return (
    <main className="mx-auto max-w-2xl space-y-6 p-6">
      <h1 className="text-2xl font-semibold">Settings</h1>
      <section className="rounded border p-4">
        <h2 className="font-medium">Profile</h2>
        <p>{account.displayName}</p>
        <p>{account.email}</p>
      </section>
      <section className="rounded border p-4">
        <h2 className="font-medium">Notifications</h2>
        <ul>
          {Object.entries(prefs).map(([name, enabled]) => (
            <li key={name}>
              {name}: {enabled ? "on" : "off"}
            </li>
          ))}
        </ul>
      </section>
      <section className="rounded border p-4">
        <h2 className="font-medium">Danger zone</h2>
        <button className="rounded bg-red-600 px-3 py-1 text-white">Close account</button>
      </section>
    </main>
  );
}

# Notification architecture reference

The existing assignment flow publishes task events. Keep its event identity.
The existing email provider adapter owns provider IO and delivery results.
Use that adapter; do not add another transport, queue or provider framework.
Preferences belong to the application; feature state and job deduplication
must be checked before a send. Delivery status belongs to the delivery owner.

Extend the real assignment journey first, then the existing overdue flow.
The rollout must preserve opt-out behavior and the disabled sending flag.
No notification history UI or message-body storage is part of this design.

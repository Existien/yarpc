/* Generated by YARPC
 * Version:  0.1.0
 * Definition:
 *   File: /workspace/tests/definitions/01_minimal.yml
 *   Object: Minimal
 *   Template: qt6/client_header.j2
 */
#pragma once
#include <QObject>
#include <qqmlintegration.h>
#include <QDBusMessage>
#include <QDBusServiceWatcher>
#include <QDBusPendingCallWatcher>
#include <QVariant>
#include "DBusError.hpp"
#include "types.hpp"
namespace gen::minimal {

namespace BackendMinimalClientUtils {

/**
 * @brief Pending call object for the Bump method calls.
 */
class BumpPendingCall : public QObject {
    Q_OBJECT
    QML_UNCREATABLE("")
    QML_ELEMENT
public:
    BumpPendingCall(QDBusPendingCall pendingCall, QObject *parent);
signals:
    /**
     * @brief Emitted when an Bump call returns.
     */
    void finished();

    /**
     * @brief Emitted when an error ocurred during an Bump call.
     *
     * @param error the error
     */
    void error(DBusError error);
private slots:
    void callFinished(QDBusPendingCallWatcher *watcher);
private:
    QDBusPendingCallWatcher m_watcher;
};

}

/**
 * D-Bus client for the com.yarpc.backend.minimal D-Bus interface
 */
class BackendMinimalClient : public QObject {
    Q_OBJECT
    QML_ELEMENT
    /**
     * @brief Whether the client is connected.
     */
    Q_PROPERTY(bool connected READ getConnected NOTIFY connectedChanged)
public:
    BackendMinimalClient(QObject* parent = nullptr);

public slots:
    /**
     * @brief Returns whether the target service is available.
     *
     * @returns Whether the target service is available.
     */
    bool getConnected() const;

    /**
     * @brief Returns a map containing the current values of all properties.
     *
     * @returns a map containing the current values of all properties
     */
    QVariantMap getAllProperties() const;

    /**
     * @brief a simple method without args
     *
     * @returns Pending call object with finished signal containing the reply.
     */
    BackendMinimalClientUtils::BumpPendingCall* Bump(
    );

signals:
    /**
     * @brief Emitted when the connected property changes.
     */
    void connectedChanged();

    /**
     * @brief a simple signal without arguments
     */
    void bumpedReceived(
    );

private slots:
    void connectedHandler(const QString& service);
    void disconnectedHandler(const QString& service);
    void propertiesChangedHandler(QString interface, QVariantMap changes, QStringList);
    void BumpedDBusHandler(QDBusMessage content);
private:
    bool m_connected = false;
    QDBusServiceWatcher m_watcher;
};

}
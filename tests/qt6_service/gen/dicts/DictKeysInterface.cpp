/* Generated by YARPC
 * Version:  0.1.0
 * Definition:
 *   File: /workspace/tests/definitions/05.4_dictionaries_keys.yml
 *   Object: DictKeys
 *   Template: qt6/service_source.j2
 */
#include <QDBusArgument>
#include "DictKeysInterface.hpp"
#include "DictKeysInterfaceAdaptor.hpp"
#include "Connection.hpp"
#include "types.hpp"

using namespace gen::dicts;

DictKeysInterface::DictKeysInterface(QObject* parent)
: QObject(parent) {
    registerMetaTypes();
    QObject::connect(
        &Connection::instance(),
        &Connection::connectedChanged,
        this,
        &DictKeysInterface::connectedChanged
    );
    QObject::connect(
        &Connection::instance(),
        &Connection::registrationChanged,
        this,
        &DictKeysInterface::connectedChanged
    );
}

void DictKeysInterface::connect() {
    Connection::instance().registerDictKeys(this);
}

void DictKeysInterface::disconnect() {
    Connection::instance().unregisterDictKeys();
}

void DictKeysInterface::finishCall(const QDBusMessage &reply)
{
    Connection::instance().send(reply);
}

bool DictKeysInterface::getConnected() const {
    return (
        Connection::instance().getConnected()
        && Connection::instance().isDictKeysRegistered()
    );
}

void DictKeysInterface::EmitUint8Signal(
    QMap<uchar, QString> value
) {
    if (Connection::instance().DictKeys() != nullptr ) {
        emit Connection::instance().DictKeys()->Uint8Signal(
            value
        );
    }
}

void DictKeysInterface::EmitUint8Signal(
    QVariant value
) {
    QMap<uchar, QString> arg_0;
    arg_0 = value.value<QMap<uchar, QString>>();

    EmitUint8Signal(
        arg_0
    );
}

void DictKeysInterface::EmitBoolSignal(
    QMap<bool, QString> value
) {
    if (Connection::instance().DictKeys() != nullptr ) {
        emit Connection::instance().DictKeys()->BoolSignal(
            value
        );
    }
}

void DictKeysInterface::EmitBoolSignal(
    QVariant value
) {
    QMap<bool, QString> arg_0;
    arg_0 = value.value<QMap<bool, QString>>();

    EmitBoolSignal(
        arg_0
    );
}

void DictKeysInterface::EmitInt16Signal(
    QMap<short, QString> value
) {
    if (Connection::instance().DictKeys() != nullptr ) {
        emit Connection::instance().DictKeys()->Int16Signal(
            value
        );
    }
}

void DictKeysInterface::EmitInt16Signal(
    QVariant value
) {
    QMap<short, QString> arg_0;
    arg_0 = value.value<QMap<short, QString>>();

    EmitInt16Signal(
        arg_0
    );
}

void DictKeysInterface::EmitUint16Signal(
    QMap<ushort, QString> value
) {
    if (Connection::instance().DictKeys() != nullptr ) {
        emit Connection::instance().DictKeys()->Uint16Signal(
            value
        );
    }
}

void DictKeysInterface::EmitUint16Signal(
    QVariant value
) {
    QMap<ushort, QString> arg_0;
    arg_0 = value.value<QMap<ushort, QString>>();

    EmitUint16Signal(
        arg_0
    );
}

void DictKeysInterface::EmitInt32Signal(
    QMap<int, QString> value
) {
    if (Connection::instance().DictKeys() != nullptr ) {
        emit Connection::instance().DictKeys()->Int32Signal(
            value
        );
    }
}

void DictKeysInterface::EmitInt32Signal(
    QVariant value
) {
    QMap<int, QString> arg_0;
    arg_0 = value.value<QMap<int, QString>>();

    EmitInt32Signal(
        arg_0
    );
}

void DictKeysInterface::EmitUint32Signal(
    QMap<uint, QString> value
) {
    if (Connection::instance().DictKeys() != nullptr ) {
        emit Connection::instance().DictKeys()->Uint32Signal(
            value
        );
    }
}

void DictKeysInterface::EmitUint32Signal(
    QVariant value
) {
    QMap<uint, QString> arg_0;
    arg_0 = value.value<QMap<uint, QString>>();

    EmitUint32Signal(
        arg_0
    );
}

void DictKeysInterface::EmitInt64Signal(
    QMap<qlonglong, QString> value
) {
    if (Connection::instance().DictKeys() != nullptr ) {
        emit Connection::instance().DictKeys()->Int64Signal(
            value
        );
    }
}

void DictKeysInterface::EmitInt64Signal(
    QVariant value
) {
    QMap<qlonglong, QString> arg_0;
    arg_0 = value.value<QMap<qlonglong, QString>>();

    EmitInt64Signal(
        arg_0
    );
}

void DictKeysInterface::EmitUint64Signal(
    QMap<qulonglong, QString> value
) {
    if (Connection::instance().DictKeys() != nullptr ) {
        emit Connection::instance().DictKeys()->Uint64Signal(
            value
        );
    }
}

void DictKeysInterface::EmitUint64Signal(
    QVariant value
) {
    QMap<qulonglong, QString> arg_0;
    arg_0 = value.value<QMap<qulonglong, QString>>();

    EmitUint64Signal(
        arg_0
    );
}

void DictKeysInterface::EmitDoubleSignal(
    QMap<double, QString> value
) {
    if (Connection::instance().DictKeys() != nullptr ) {
        emit Connection::instance().DictKeys()->DoubleSignal(
            value
        );
    }
}

void DictKeysInterface::EmitDoubleSignal(
    QVariant value
) {
    QMap<double, QString> arg_0;
    arg_0 = value.value<QMap<double, QString>>();

    EmitDoubleSignal(
        arg_0
    );
}

void DictKeysInterface::EmitStringSignal(
    QMap<QString, QString> value
) {
    if (Connection::instance().DictKeys() != nullptr ) {
        emit Connection::instance().DictKeys()->StringSignal(
            value
        );
    }
}

void DictKeysInterface::EmitStringSignal(
    QVariant value
) {
    QMap<QString, QString> arg_0;
    arg_0 = value.value<QMap<QString, QString>>();

    EmitStringSignal(
        arg_0
    );
}

Uint8MethodPendingReply::Uint8MethodPendingReply(QDBusMessage call, QObject *parent) : QObject(parent) {
    m_call = call;
    QMap<uchar, QString> arg_0;
    {
        auto marshalled = m_call.arguments()[0].value<QDBusArgument>();
        marshalled >> arg_0;
    }
    m_args = Uint8MethodArgs{
        .value = static_cast<QMap<uchar, QString>>(arg_0),
    };
}

Uint8MethodArgs Uint8MethodPendingReply::args() {
    return m_args;
}

void Uint8MethodPendingReply::sendReply(
    QVariant reply
) {
    QMap<uchar, QString> unmarshalled;
    unmarshalled = reply.value<QMap<uchar, QString>>();

    sendReply(unmarshalled);
}

void Uint8MethodPendingReply::sendReply(
    const QMap<uchar, QString> &reply
) {
    auto replyToSend = static_cast<QMap<uchar, QString>>(reply);
    auto dbusReply = m_call.createReply(QVariant::fromValue(replyToSend));
    auto iface = dynamic_cast<DictKeysInterface*>(parent());
    if (iface != nullptr) {
        iface->finishCall(dbusReply);
    }
    deleteLater();
}

void Uint8MethodPendingReply::sendError(const QString& name, const QString& message) {
    auto error_reply = m_call.createErrorReply(name, message);
    auto iface = dynamic_cast<DictKeysInterface*>(parent());
    if (iface != nullptr) {
        iface->finishCall(error_reply);
    }
    deleteLater();
}

void Uint8MethodPendingReply::sendError(const DBusError &error) {
    auto error_reply = m_call.createErrorReply(error);
    auto iface = dynamic_cast<DictKeysInterface*>(parent());
    if (iface != nullptr) {
        iface->finishCall(error_reply);
    }
    deleteLater();
}

void DictKeysInterface::handleUint8MethodCalled(QDBusMessage call) {
    auto reply = new Uint8MethodPendingReply(call, this);
    emit uint8MethodCalled(reply);
}

BoolMethodPendingReply::BoolMethodPendingReply(QDBusMessage call, QObject *parent) : QObject(parent) {
    m_call = call;
    QMap<bool, QString> arg_0;
    {
        auto marshalled = m_call.arguments()[0].value<QDBusArgument>();
        marshalled >> arg_0;
    }
    m_args = BoolMethodArgs{
        .value = static_cast<QMap<bool, QString>>(arg_0),
    };
}

BoolMethodArgs BoolMethodPendingReply::args() {
    return m_args;
}

void BoolMethodPendingReply::sendReply(
    QVariant reply
) {
    QMap<bool, QString> unmarshalled;
    unmarshalled = reply.value<QMap<bool, QString>>();

    sendReply(unmarshalled);
}

void BoolMethodPendingReply::sendReply(
    const QMap<bool, QString> &reply
) {
    auto replyToSend = static_cast<QMap<bool, QString>>(reply);
    auto dbusReply = m_call.createReply(QVariant::fromValue(replyToSend));
    auto iface = dynamic_cast<DictKeysInterface*>(parent());
    if (iface != nullptr) {
        iface->finishCall(dbusReply);
    }
    deleteLater();
}

void BoolMethodPendingReply::sendError(const QString& name, const QString& message) {
    auto error_reply = m_call.createErrorReply(name, message);
    auto iface = dynamic_cast<DictKeysInterface*>(parent());
    if (iface != nullptr) {
        iface->finishCall(error_reply);
    }
    deleteLater();
}

void BoolMethodPendingReply::sendError(const DBusError &error) {
    auto error_reply = m_call.createErrorReply(error);
    auto iface = dynamic_cast<DictKeysInterface*>(parent());
    if (iface != nullptr) {
        iface->finishCall(error_reply);
    }
    deleteLater();
}

void DictKeysInterface::handleBoolMethodCalled(QDBusMessage call) {
    auto reply = new BoolMethodPendingReply(call, this);
    emit boolMethodCalled(reply);
}

Int16MethodPendingReply::Int16MethodPendingReply(QDBusMessage call, QObject *parent) : QObject(parent) {
    m_call = call;
    QMap<short, QString> arg_0;
    {
        auto marshalled = m_call.arguments()[0].value<QDBusArgument>();
        marshalled >> arg_0;
    }
    m_args = Int16MethodArgs{
        .value = static_cast<QMap<short, QString>>(arg_0),
    };
}

Int16MethodArgs Int16MethodPendingReply::args() {
    return m_args;
}

void Int16MethodPendingReply::sendReply(
    QVariant reply
) {
    QMap<short, QString> unmarshalled;
    unmarshalled = reply.value<QMap<short, QString>>();

    sendReply(unmarshalled);
}

void Int16MethodPendingReply::sendReply(
    const QMap<short, QString> &reply
) {
    auto replyToSend = static_cast<QMap<short, QString>>(reply);
    auto dbusReply = m_call.createReply(QVariant::fromValue(replyToSend));
    auto iface = dynamic_cast<DictKeysInterface*>(parent());
    if (iface != nullptr) {
        iface->finishCall(dbusReply);
    }
    deleteLater();
}

void Int16MethodPendingReply::sendError(const QString& name, const QString& message) {
    auto error_reply = m_call.createErrorReply(name, message);
    auto iface = dynamic_cast<DictKeysInterface*>(parent());
    if (iface != nullptr) {
        iface->finishCall(error_reply);
    }
    deleteLater();
}

void Int16MethodPendingReply::sendError(const DBusError &error) {
    auto error_reply = m_call.createErrorReply(error);
    auto iface = dynamic_cast<DictKeysInterface*>(parent());
    if (iface != nullptr) {
        iface->finishCall(error_reply);
    }
    deleteLater();
}

void DictKeysInterface::handleInt16MethodCalled(QDBusMessage call) {
    auto reply = new Int16MethodPendingReply(call, this);
    emit int16MethodCalled(reply);
}

Uint16MethodPendingReply::Uint16MethodPendingReply(QDBusMessage call, QObject *parent) : QObject(parent) {
    m_call = call;
    QMap<ushort, QString> arg_0;
    {
        auto marshalled = m_call.arguments()[0].value<QDBusArgument>();
        marshalled >> arg_0;
    }
    m_args = Uint16MethodArgs{
        .value = static_cast<QMap<ushort, QString>>(arg_0),
    };
}

Uint16MethodArgs Uint16MethodPendingReply::args() {
    return m_args;
}

void Uint16MethodPendingReply::sendReply(
    QVariant reply
) {
    QMap<ushort, QString> unmarshalled;
    unmarshalled = reply.value<QMap<ushort, QString>>();

    sendReply(unmarshalled);
}

void Uint16MethodPendingReply::sendReply(
    const QMap<ushort, QString> &reply
) {
    auto replyToSend = static_cast<QMap<ushort, QString>>(reply);
    auto dbusReply = m_call.createReply(QVariant::fromValue(replyToSend));
    auto iface = dynamic_cast<DictKeysInterface*>(parent());
    if (iface != nullptr) {
        iface->finishCall(dbusReply);
    }
    deleteLater();
}

void Uint16MethodPendingReply::sendError(const QString& name, const QString& message) {
    auto error_reply = m_call.createErrorReply(name, message);
    auto iface = dynamic_cast<DictKeysInterface*>(parent());
    if (iface != nullptr) {
        iface->finishCall(error_reply);
    }
    deleteLater();
}

void Uint16MethodPendingReply::sendError(const DBusError &error) {
    auto error_reply = m_call.createErrorReply(error);
    auto iface = dynamic_cast<DictKeysInterface*>(parent());
    if (iface != nullptr) {
        iface->finishCall(error_reply);
    }
    deleteLater();
}

void DictKeysInterface::handleUint16MethodCalled(QDBusMessage call) {
    auto reply = new Uint16MethodPendingReply(call, this);
    emit uint16MethodCalled(reply);
}

Int32MethodPendingReply::Int32MethodPendingReply(QDBusMessage call, QObject *parent) : QObject(parent) {
    m_call = call;
    QMap<int, QString> arg_0;
    {
        auto marshalled = m_call.arguments()[0].value<QDBusArgument>();
        marshalled >> arg_0;
    }
    m_args = Int32MethodArgs{
        .value = static_cast<QMap<int, QString>>(arg_0),
    };
}

Int32MethodArgs Int32MethodPendingReply::args() {
    return m_args;
}

void Int32MethodPendingReply::sendReply(
    QVariant reply
) {
    QMap<int, QString> unmarshalled;
    unmarshalled = reply.value<QMap<int, QString>>();

    sendReply(unmarshalled);
}

void Int32MethodPendingReply::sendReply(
    const QMap<int, QString> &reply
) {
    auto replyToSend = static_cast<QMap<int, QString>>(reply);
    auto dbusReply = m_call.createReply(QVariant::fromValue(replyToSend));
    auto iface = dynamic_cast<DictKeysInterface*>(parent());
    if (iface != nullptr) {
        iface->finishCall(dbusReply);
    }
    deleteLater();
}

void Int32MethodPendingReply::sendError(const QString& name, const QString& message) {
    auto error_reply = m_call.createErrorReply(name, message);
    auto iface = dynamic_cast<DictKeysInterface*>(parent());
    if (iface != nullptr) {
        iface->finishCall(error_reply);
    }
    deleteLater();
}

void Int32MethodPendingReply::sendError(const DBusError &error) {
    auto error_reply = m_call.createErrorReply(error);
    auto iface = dynamic_cast<DictKeysInterface*>(parent());
    if (iface != nullptr) {
        iface->finishCall(error_reply);
    }
    deleteLater();
}

void DictKeysInterface::handleInt32MethodCalled(QDBusMessage call) {
    auto reply = new Int32MethodPendingReply(call, this);
    emit int32MethodCalled(reply);
}

Uint32MethodPendingReply::Uint32MethodPendingReply(QDBusMessage call, QObject *parent) : QObject(parent) {
    m_call = call;
    QMap<uint, QString> arg_0;
    {
        auto marshalled = m_call.arguments()[0].value<QDBusArgument>();
        marshalled >> arg_0;
    }
    m_args = Uint32MethodArgs{
        .value = static_cast<QMap<uint, QString>>(arg_0),
    };
}

Uint32MethodArgs Uint32MethodPendingReply::args() {
    return m_args;
}

void Uint32MethodPendingReply::sendReply(
    QVariant reply
) {
    QMap<uint, QString> unmarshalled;
    unmarshalled = reply.value<QMap<uint, QString>>();

    sendReply(unmarshalled);
}

void Uint32MethodPendingReply::sendReply(
    const QMap<uint, QString> &reply
) {
    auto replyToSend = static_cast<QMap<uint, QString>>(reply);
    auto dbusReply = m_call.createReply(QVariant::fromValue(replyToSend));
    auto iface = dynamic_cast<DictKeysInterface*>(parent());
    if (iface != nullptr) {
        iface->finishCall(dbusReply);
    }
    deleteLater();
}

void Uint32MethodPendingReply::sendError(const QString& name, const QString& message) {
    auto error_reply = m_call.createErrorReply(name, message);
    auto iface = dynamic_cast<DictKeysInterface*>(parent());
    if (iface != nullptr) {
        iface->finishCall(error_reply);
    }
    deleteLater();
}

void Uint32MethodPendingReply::sendError(const DBusError &error) {
    auto error_reply = m_call.createErrorReply(error);
    auto iface = dynamic_cast<DictKeysInterface*>(parent());
    if (iface != nullptr) {
        iface->finishCall(error_reply);
    }
    deleteLater();
}

void DictKeysInterface::handleUint32MethodCalled(QDBusMessage call) {
    auto reply = new Uint32MethodPendingReply(call, this);
    emit uint32MethodCalled(reply);
}

Int64MethodPendingReply::Int64MethodPendingReply(QDBusMessage call, QObject *parent) : QObject(parent) {
    m_call = call;
    QMap<qlonglong, QString> arg_0;
    {
        auto marshalled = m_call.arguments()[0].value<QDBusArgument>();
        marshalled >> arg_0;
    }
    m_args = Int64MethodArgs{
        .value = static_cast<QMap<qlonglong, QString>>(arg_0),
    };
}

Int64MethodArgs Int64MethodPendingReply::args() {
    return m_args;
}

void Int64MethodPendingReply::sendReply(
    QVariant reply
) {
    QMap<qlonglong, QString> unmarshalled;
    unmarshalled = reply.value<QMap<qlonglong, QString>>();

    sendReply(unmarshalled);
}

void Int64MethodPendingReply::sendReply(
    const QMap<qlonglong, QString> &reply
) {
    auto replyToSend = static_cast<QMap<qlonglong, QString>>(reply);
    auto dbusReply = m_call.createReply(QVariant::fromValue(replyToSend));
    auto iface = dynamic_cast<DictKeysInterface*>(parent());
    if (iface != nullptr) {
        iface->finishCall(dbusReply);
    }
    deleteLater();
}

void Int64MethodPendingReply::sendError(const QString& name, const QString& message) {
    auto error_reply = m_call.createErrorReply(name, message);
    auto iface = dynamic_cast<DictKeysInterface*>(parent());
    if (iface != nullptr) {
        iface->finishCall(error_reply);
    }
    deleteLater();
}

void Int64MethodPendingReply::sendError(const DBusError &error) {
    auto error_reply = m_call.createErrorReply(error);
    auto iface = dynamic_cast<DictKeysInterface*>(parent());
    if (iface != nullptr) {
        iface->finishCall(error_reply);
    }
    deleteLater();
}

void DictKeysInterface::handleInt64MethodCalled(QDBusMessage call) {
    auto reply = new Int64MethodPendingReply(call, this);
    emit int64MethodCalled(reply);
}

Uint64MethodPendingReply::Uint64MethodPendingReply(QDBusMessage call, QObject *parent) : QObject(parent) {
    m_call = call;
    QMap<qulonglong, QString> arg_0;
    {
        auto marshalled = m_call.arguments()[0].value<QDBusArgument>();
        marshalled >> arg_0;
    }
    m_args = Uint64MethodArgs{
        .value = static_cast<QMap<qulonglong, QString>>(arg_0),
    };
}

Uint64MethodArgs Uint64MethodPendingReply::args() {
    return m_args;
}

void Uint64MethodPendingReply::sendReply(
    QVariant reply
) {
    QMap<qulonglong, QString> unmarshalled;
    unmarshalled = reply.value<QMap<qulonglong, QString>>();

    sendReply(unmarshalled);
}

void Uint64MethodPendingReply::sendReply(
    const QMap<qulonglong, QString> &reply
) {
    auto replyToSend = static_cast<QMap<qulonglong, QString>>(reply);
    auto dbusReply = m_call.createReply(QVariant::fromValue(replyToSend));
    auto iface = dynamic_cast<DictKeysInterface*>(parent());
    if (iface != nullptr) {
        iface->finishCall(dbusReply);
    }
    deleteLater();
}

void Uint64MethodPendingReply::sendError(const QString& name, const QString& message) {
    auto error_reply = m_call.createErrorReply(name, message);
    auto iface = dynamic_cast<DictKeysInterface*>(parent());
    if (iface != nullptr) {
        iface->finishCall(error_reply);
    }
    deleteLater();
}

void Uint64MethodPendingReply::sendError(const DBusError &error) {
    auto error_reply = m_call.createErrorReply(error);
    auto iface = dynamic_cast<DictKeysInterface*>(parent());
    if (iface != nullptr) {
        iface->finishCall(error_reply);
    }
    deleteLater();
}

void DictKeysInterface::handleUint64MethodCalled(QDBusMessage call) {
    auto reply = new Uint64MethodPendingReply(call, this);
    emit uint64MethodCalled(reply);
}

DoubleMethodPendingReply::DoubleMethodPendingReply(QDBusMessage call, QObject *parent) : QObject(parent) {
    m_call = call;
    QMap<double, QString> arg_0;
    {
        auto marshalled = m_call.arguments()[0].value<QDBusArgument>();
        marshalled >> arg_0;
    }
    m_args = DoubleMethodArgs{
        .value = static_cast<QMap<double, QString>>(arg_0),
    };
}

DoubleMethodArgs DoubleMethodPendingReply::args() {
    return m_args;
}

void DoubleMethodPendingReply::sendReply(
    QVariant reply
) {
    QMap<double, QString> unmarshalled;
    unmarshalled = reply.value<QMap<double, QString>>();

    sendReply(unmarshalled);
}

void DoubleMethodPendingReply::sendReply(
    const QMap<double, QString> &reply
) {
    auto replyToSend = static_cast<QMap<double, QString>>(reply);
    auto dbusReply = m_call.createReply(QVariant::fromValue(replyToSend));
    auto iface = dynamic_cast<DictKeysInterface*>(parent());
    if (iface != nullptr) {
        iface->finishCall(dbusReply);
    }
    deleteLater();
}

void DoubleMethodPendingReply::sendError(const QString& name, const QString& message) {
    auto error_reply = m_call.createErrorReply(name, message);
    auto iface = dynamic_cast<DictKeysInterface*>(parent());
    if (iface != nullptr) {
        iface->finishCall(error_reply);
    }
    deleteLater();
}

void DoubleMethodPendingReply::sendError(const DBusError &error) {
    auto error_reply = m_call.createErrorReply(error);
    auto iface = dynamic_cast<DictKeysInterface*>(parent());
    if (iface != nullptr) {
        iface->finishCall(error_reply);
    }
    deleteLater();
}

void DictKeysInterface::handleDoubleMethodCalled(QDBusMessage call) {
    auto reply = new DoubleMethodPendingReply(call, this);
    emit doubleMethodCalled(reply);
}

StringMethodPendingReply::StringMethodPendingReply(QDBusMessage call, QObject *parent) : QObject(parent) {
    m_call = call;
    QMap<QString, QString> arg_0;
    {
        auto marshalled = m_call.arguments()[0].value<QDBusArgument>();
        marshalled >> arg_0;
    }
    m_args = StringMethodArgs{
        .value = static_cast<QMap<QString, QString>>(arg_0),
    };
}

StringMethodArgs StringMethodPendingReply::args() {
    return m_args;
}

void StringMethodPendingReply::sendReply(
    QVariant reply
) {
    QMap<QString, QString> unmarshalled;
    unmarshalled = reply.value<QMap<QString, QString>>();

    sendReply(unmarshalled);
}

void StringMethodPendingReply::sendReply(
    const QMap<QString, QString> &reply
) {
    auto replyToSend = static_cast<QMap<QString, QString>>(reply);
    auto dbusReply = m_call.createReply(QVariant::fromValue(replyToSend));
    auto iface = dynamic_cast<DictKeysInterface*>(parent());
    if (iface != nullptr) {
        iface->finishCall(dbusReply);
    }
    deleteLater();
}

void StringMethodPendingReply::sendError(const QString& name, const QString& message) {
    auto error_reply = m_call.createErrorReply(name, message);
    auto iface = dynamic_cast<DictKeysInterface*>(parent());
    if (iface != nullptr) {
        iface->finishCall(error_reply);
    }
    deleteLater();
}

void StringMethodPendingReply::sendError(const DBusError &error) {
    auto error_reply = m_call.createErrorReply(error);
    auto iface = dynamic_cast<DictKeysInterface*>(parent());
    if (iface != nullptr) {
        iface->finishCall(error_reply);
    }
    deleteLater();
}

void DictKeysInterface::handleStringMethodCalled(QDBusMessage call) {
    auto reply = new StringMethodPendingReply(call, this);
    emit stringMethodCalled(reply);
}


void DictKeysInterface::emitPropertiesChangedSignal(const QVariantMap &changedProps) {
    auto signal = QDBusMessage::createSignal(
        "/com/yarpc/testservice/dicts",
        "org.freedesktop.DBus.Properties",
        "PropertiesChanged"
    );
    signal << "com.yarpc.testservice.dictKeys";
    signal << changedProps;
    signal << QStringList{};
    Connection::instance().send(signal);
}